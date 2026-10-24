---
name: unknown_workflow_upscale_latent_upscale_lora_69
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.895333
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, Int, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/work_one（图生视频工作流）_2056265109323993089.json, 视频生成/图生视频/【运镜+自动脚本】图生视频 LTXV 2.0-19B 测试版_2008778999371145217.json, 视频生成/图生视频/图生视频  音画同步  带多种电影级别运镜 LTXV 2.0_2025763431185387521.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_69

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/work_one（图生视频工作流）_2056265109323993089.json、视频生成/图生视频/【运镜+自动脚本】图生视频 LTXV 2.0-19B 测试版_2008778999371145217.json、视频生成/图生视频/图生视频  音画同步  带多种电影级别运镜 LTXV 2.0_2025763431185387521.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `Int`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Text Replace` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `LTXVImgToVideoInplace` —— 2/3 个有
- `ManualSigmas` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `SamplerCustom` —— 2/3 个有
- `Textbox` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `intToFloat _O` —— 2/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `LTXVImgToVideoInplaceKJ` —— 1/3 个有
- `TextGenerateLTX2Prompt` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 0.3 | - | 1 | 100% |
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
