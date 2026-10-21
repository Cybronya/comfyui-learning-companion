---
name: unknown_workflow_video_lora_sampler_329
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.860857
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DF_Integer, ImageStitch, KSamplerAdvanced, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveBoolean, RH_Captioner, RH_Translator, SimpleMath+, Textbox, UNETLoader, VAEDecode, VAELoader, WanFirstLastFrameToVideo, WanVideoNAG, easy ifElse, easy showAnything]
problems: []
missing: [LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+]
members: [视频生成/图生视频/1962663438763864066.json, 视频生成/图生视频/1962700232851079170.json, 视频生成/图生视频/1962711139945693186.json, 视频生成/图生视频/1980870124980883457.json, 视频生成/图生视频/1953264149745889282.json, 视频生成/文生视频/1957688772295061505.json, 视频生成/文生视频/1957693851249078273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_329

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1962663438763864066.json、视频生成/图生视频/1962700232851079170.json、视频生成/图生视频/1962711139945693186.json、视频生成/图生视频/1980870124980883457.json、视频生成/图生视频/1953264149745889282.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DF_Integer`
- `ImageStitch`
- `KSamplerAdvanced`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `RH_Captioner`
- `RH_Translator`
- `SimpleMath+`
- `Textbox`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanFirstLastFrameToVideo`
- `WanVideoNAG`
- `easy ifElse`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `RH_Nano_Banana_Image2Image` —— 4/7 个有
- `SaveVideo` —— 4/7 个有
- `CR Upscale Image` —— 3/7 个有
- `RIFE VFI` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `TextCombinerSix` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 7 | 100% |
| 采样算法 | 4 | 4 - 4 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageMaskScaleAs、LayerUtility: ImageScaleByAspectRatio V2、SimpleMath+
