---
name: unknown_workflow_video_sampler_vae_150
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.906667
common_nodes: [CLIPLoader, CR Prompt Text, CreateVideo, GetVideoComponents, InteractAvatar_SM_Model, InteractAvatar_SM_Predata, InteractAvatar_SM_Sampler, JWInteger, LoadAudio, LoadImage, SaveImage, SaveVideo, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/InteractAvatar 可与环境交互的数字人_2032281345518473217.json, 数字人/数字人/InteractAvatar与环境交互的具身数字人（AP2V）_2030597535340957698.json, 视频生成/图生视频/InteractAvatar与环境交互的具身数字人（AI2V）_2031728952187822082.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_150

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/InteractAvatar 可与环境交互的数字人_2032281345518473217.json、数字人/数字人/InteractAvatar与环境交互的具身数字人（AP2V）_2030597535340957698.json、视频生成/图生视频/InteractAvatar与环境交互的具身数字人（AI2V）_2031728952187822082.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `CreateVideo`
- `GetVideoComponents`
- `InteractAvatar_SM_Model`
- `InteractAvatar_SM_Predata`
- `InteractAvatar_SM_Sampler`
- `JWInteger`
- `LoadAudio`
- `LoadImage`
- `SaveImage`
- `SaveVideo`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AILab_MaskOverlay` —— 2/3 个有
- `DWPreprocessor` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `MaskPreview` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `LoadVideo` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
