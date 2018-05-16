def allocate_lock():
  lock = DummyThreadLock()
class DummyThreadLock:
  def acquire(self):
    print("DummyThreadLock.acquire")
  def release(self):
    print("DummyThreadLock.release")