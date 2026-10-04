# Pattern Evolution

记录 Pattern 的演化规则：当新 workflow 在已知 Pattern 基础上出现扩展节点时，
判定为该 Pattern 的 Extension，形成新 Pattern。

---

## 演化规则

1. 新 workflow 与已知 Pattern 的节点集合对比（见 `engine/workflow_index_manager.py` 的 `find_similar_workflows()` 与 `skills/comfyui-learning/tools/compare_workflow.py`）。
2. 无节点增删 → **same pattern**。
3. 出现扩展节点（如 LoRA / ControlNet / IPAdapter）→ 在基础 Pattern 上叠加 Extension，产生 **new pattern**。
4. 新 Pattern 命名：`基础-pattern + 扩展名`，并写入 workflow index。

---

## 记录格式

```text
Pattern Evolution

Basic:
    <基础 Pattern>

Extension:
    + <扩展 1>
    + <扩展 2>

Result:
    New Pattern
```

---

## 示例

### SD1.5 Text2Image → + LoRA

```text
Pattern Evolution

Basic:
    SD1.5 Text2Image (sd15-t2i-basic)

Extension:
    + LoRA (LoraLoader)

Result:
    New Pattern (sd15-t2i-lora)
```

### SD1.5 Text2Image → + LoRA + ControlNet + IPAdapter

```text
Pattern Evolution

Basic:
    SD1.5 Text2Image (sd15-t2i-basic)

Extension:
    + LoRA (LoraLoader)
    + ControlNet (ControlNetLoader)
    + IPAdapter (IPAdapterAdvanced)

Result:
    New Pattern (sd15-t2i-lora-controlnet-ipadapter)
```

---

## 相关文件

| 文件 | 作用 |
|-|-|
| `engine/workflow_index_manager.py` | 维护 workflow 模式索引，`find_similar_workflows()` |
| `skills/comfyui-learning/tools/compare_workflow.py` | Node / Parameter / Pattern 三层对比 |
| `comfyui_library/knowledge/patterns/` | Pattern 知识卡存放处 |
