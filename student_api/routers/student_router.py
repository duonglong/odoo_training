from typing import Annotated, List
from fastapi import APIRouter, Depends
from odoo.api import Environment
from odoo.addons.fastapi_auth_jwt.dependencies import auth_jwt_authenticated_odoo_env
from ..schemas.student import StudentInfo, StudentCreateInfo

router = APIRouter(tags=["students"])


@router.get("/students", response_model=List[StudentInfo])
async def get_students(
        env: Annotated[Environment, Depends(auth_jwt_authenticated_odoo_env)],
) -> List[StudentInfo]:
    """Get the list of all students."""
    students = env["student.student"].search([])
    return [
        StudentInfo(
            id=student.id,
            name=student.name or None,
            date_of_birth=student.date_of_birth or None,
            age=student.age or None,
            class_room=student.class_room_id.name or None,
        )
        for student in students
    ]


@router.post("/student", response_model=StudentInfo)
async def create_student(
        studentData: StudentCreateInfo,
        env: Annotated[Environment, Depends(auth_jwt_authenticated_odoo_env)]
) -> StudentInfo:
    env["student.student"].with_delay().create({
        'name': studentData.name,
        'date_of_birth': studentData.date_of_birth,
    })
    return StudentInfo(
        id=123,
        name=None,
        date_of_birth=None,
        age= None
    )
