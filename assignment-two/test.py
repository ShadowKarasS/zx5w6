import pytest
import manage

def test_admin():
    admin_status = manage.check_admin()
    assert admin_status == 'true'

def test_admin_f():
    admin_status = manage.check_admin()
    assert admin_statue == 'false'

def test_instru():
    instructor_status = manage.check_instru()
    assert instructor_status == 'true'

def test_instru_f():
    insturctor_statue = manage.check_instru()
    assert instructor_status == 'false'

def test_remove():
    have_course = manage.check_remove()
    assert have_course == 'true'

def test_remove_f():
    have_course = manage.check_remove()
    assert have_course == 'false'

def test_disable():
    course_status = manage.check_disable()
    assert course_status == 'active'

def test_disable_f():
    course_status = manage.check_disable()
    assert course_status == 'not-active'

def test_save():
    new_change_saved = manage.check_save()
    assert new_change_saved == 'true'

def test_save_f():
    new_change_saved = manage.check_save()
    assert new_change_saved == 'false'



