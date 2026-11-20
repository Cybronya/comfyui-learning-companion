---
name: unknown_workflow_video_upscale_latent_upscale_60
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 1
common_nodes: [GetVideoComponents, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadVideo, ManualSigmas, MiniMaxH3LatentUpscaleBy32T8, RH_HeyGemNode, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEEncode, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/数字人工作流2.0_2100529234358915073.json, 数字人/数字人/数字人工作流3.0_2100543410036887554.json, 数字人/数字人/数字人工作流_2100519010789052417.json, 音频生成/音频生成/声音克隆_2100632305353187330.json, 音频生成/音频生成/数字人工作流3.0_2103301033215741954.json, 音频生成/音频生成/数字人工作流3.0_2104851029266358273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_60

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/数字人工作流2.0_2100529234358915073.json、数字人/数字人/数字人工作流3.0_2100543410036887554.json、数字人/数字人/数字人工作流_2100519010789052417.json、音频生成/音频生成/声音克隆_2100632305353187330.json、音频生成/音频生成/数字人工作流3.0_2103301033215741954.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 6 个 workflow 都包含：
- `GetVideoComponents`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadVideo`
- `ManualSigmas`
- `MiniMaxH3LatentUpscaleBy32T8`
- `RH_HeyGemNode`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEEncode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 5/6 个有
- `Qwen3ASRLoader` —— 5/6 个有
- `Qwen3ASRTranscribe` —— 5/6 个有
- `RunningHub_VoxCPM_Generate` —— 5/6 个有
- `RunningHub_VoxCPM_LoadModel` —— 5/6 个有
- `SaveAudio` —— 4/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
