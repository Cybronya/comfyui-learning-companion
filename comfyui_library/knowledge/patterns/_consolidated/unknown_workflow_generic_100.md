---
name: unknown_workflow_generic_100
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.872444
common_nodes: [CR Prompt Text, JWInteger, LoadImage, PreviewAny, RH_MagiHumanGenerate, RH_MagiHumanModelLoader, SaveVideo, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [视频生成/图生视频/2037449795937243137.json, 视频生成/图生视频/2037446558546927617.json, 视频生成/图生视频/2037748338019278849.json, 视频生成/图生视频/2038532869190062082.json, 视频生成/图生视频/2038925657266196481.json, 视频生成/图生视频/2059211762397966338.json, 视频生成/图生视频/2038096687511638017.json, 视频生成/图生视频/2038078503165366274.json, 视频生成/图生视频/2037758920298602497.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_100

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2037449795937243137.json、视频生成/图生视频/2037446558546927617.json、视频生成/图生视频/2037748338019278849.json、视频生成/图生视频/2038532869190062082.json、视频生成/图生视频/2038925657266196481.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `CR Prompt Text`
- `JWInteger`
- `LoadImage`
- `PreviewAny`
- `RH_MagiHumanGenerate`
- `RH_MagiHumanModelLoader`
- `SaveVideo`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 5/9 个有
- `ImageResize+` —— 2/9 个有
- `Int` —— 2/9 个有
- `LayerUtility: PurgeVRAM V2` —— 2/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
