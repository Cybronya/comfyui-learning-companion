---
name: unknown_workflow_lora_sampler_unet_96
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.590889
common_nodes: [BasicGuider, ComfyMathExpression, JWImageResizeToMegapixels, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3SigmaShift, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, ViggleAnimateConditioning, ViggleTextCondLoader]
problems: []
missing: []
members: [平台全量/Viggle Animate｜视频全身换人_2119899216020590594.json, 平台全量/minimax-H3+Viggle  视频动作迁移强化版 免提示词_2119017054769602562.json, 平台全量/minimax-H3+Viggle  视频动作迁移强化版 免提示词_2119044642208567298.json, 平台全量/视频中人物替换-H3_2110651851988361217.json, 视频生成/图生视频/H3+Viggle 免提示词 【动作迁移强化版】_2105263212156514306.json, 视频生成/图生视频/H3+Viggle 免提示词 【动作迁移强化版】_2105989505089101826.json, 视频生成/图生视频/H3+Viggle 免提示词 【动作迁移强化版】_2107504505440002049.json, 视频生成/图生视频/H3+Viggle 免提示词 【动作迁移强化版】_2110281046800551937.json, 视频生成/图生视频/H3+Viggle免提示词动作迁移【画质强化版】_2105133693995151361.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_96

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/Viggle Animate｜视频全身换人_2119899216020590594.json、平台全量/minimax-H3+Viggle  视频动作迁移强化版 免提示词_2119017054769602562.json、平台全量/minimax-H3+Viggle  视频动作迁移强化版 免提示词_2119044642208567298.json、平台全量/视频中人物替换-H3_2110651851988361217.json、视频生成/图生视频/H3+Viggle 免提示词 【动作迁移强化版】_2105263212156514306.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `ComfyMathExpression`
- `JWImageResizeToMegapixels`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `ViggleAnimateConditioning`
- `ViggleTextCondLoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 8/9 个有
- `GetNode` —— 8/9 个有
- `ModelPreviewOverrideKJ` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `VHS_VideoCombine` —— 8/9 个有
- `CR Value` —— 7/9 个有
- `BlockSparseAttention` —— 1/9 个有
- `CreateVideo` —— 1/9 个有
- `GH_AudioVideoMerger` —— 1/9 个有
- `ImageScaleToTotalPixels` —— 1/9 个有
- `ManualSigmas` —— 1/9 个有
- `MuyeTextEditOutput` —— 1/9 个有
- `PrimitiveFloat` —— 1/9 个有
- `SaveVideo` —— 1/9 个有
- `SeedVR2LoadDiTModel` —— 1/9 个有
- `SeedVR2LoadVAEModel` —— 1/9 个有
- `SeedVR2VideoUpscaler` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
