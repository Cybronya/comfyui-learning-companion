---
name: unknown_workflow_generic_482
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.85
common_nodes: [Load3D, SaveGLB]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_hunyuan3d_model2uv.json, comfyui-workflow-templates-json/api_hunyuan3d_retopo_uv.json, comfyui-workflow-templates-json/api_hunyuan3d_smart_topology.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_482

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（comfyui-workflow-templates-json/api_hunyuan3d_model2uv.json、comfyui-workflow-templates-json/api_hunyuan3d_retopo_uv.json、comfyui-workflow-templates-json/api_hunyuan3d_smart_topology.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `Load3D`
- `SaveGLB`

**可变部分**（部分 workflow 才有）：
- `TencentModelTo3DUVNode` —— 2/3 个有
- `TencentSmartTopologyNode` —— 2/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
