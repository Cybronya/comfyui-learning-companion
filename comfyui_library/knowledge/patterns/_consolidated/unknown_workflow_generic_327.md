---
name: unknown_workflow_generic_327
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.879875
common_nodes: [CR Prompt Text, JWInteger, LoadImage, PreviewAny, RH_MagiHumanGenerate, RH_MagiHumanModelLoader, SaveVideo, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [数字人/数字人/（音色参考）DaVinci-MagiHuman+Qwen3.5图生视频-1_2056286130500358145.json, 视频生成/图生视频/DaVinci-MagiHuman+Qwen3.5图生视频V1（1080P）_2037449795937243137.json, 视频生成/图生视频/DaVinci-MagiHuman+Qwen3.5图生视频V1（540P）_2037446558546927617.json, 视频生成/图生视频/DaVinci-MagiHuman+Qwen3.5图生视频数字人双人对话版工作流_2037748338019278849.json, 视频生成/图生视频/Davinci magihuman 图生视频带声音_2038532869190062082.json, 视频生成/图生视频/MagiHuman 数字人 音画同步 图生视频_2038925657266196481.json, 视频生成/图生视频/MagiHuman 数字人 音画同步 图生视频_2059211762397966338.json, 视频生成/图生视频/MagiHuman+Qwen3.5自动提示词--图生音视频_2038096687511638017.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_327

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/（音色参考）DaVinci-MagiHuman+Qwen3.5图生视频-1_2056286130500358145.json、视频生成/图生视频/DaVinci-MagiHuman+Qwen3.5图生视频V1（1080P）_2037449795937243137.json、视频生成/图生视频/DaVinci-MagiHuman+Qwen3.5图生视频V1（540P）_2037446558546927617.json、视频生成/图生视频/DaVinci-MagiHuman+Qwen3.5图生视频数字人双人对话版工作流_2037748338019278849.json、视频生成/图生视频/Davinci magihuman 图生视频带声音_2038532869190062082.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
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
- `LoadAudio` —— 4/8 个有
- `ImageResize+` —— 2/8 个有
- `Int` —— 2/8 个有
- `LayerUtility: PurgeVRAM V2` —— 2/8 个有
- `MultiTextConcatenate` —— 1/8 个有
- `图像缩放V2_孤海` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
