---
name: unknown_workflow_lora_sampler_clip_137
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9115
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/人物动作控制 最优两种方法_2055642276038234114.json, 图片生成/图生图/人物换脸，开源顶级一致性flux.2 klein_2016441047668236290.json, 图片生成/图生图/哦豁看见了-Flux2-Klein_2066548615769837570.json, 图片生成/图生图/最强！人物_万物增强细节_洗图_去AI_FLUX2KLEIN_自选出图 (1)_2063478532617101314.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_137

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/人物动作控制 最优两种方法_2055642276038234114.json、图片生成/图生图/人物换脸，开源顶级一致性flux.2 klein_2016441047668236290.json、图片生成/图生图/哦豁看见了-Flux2-Klein_2066548615769837570.json、图片生成/图生图/最强！人物_万物增强细节_洗图_去AI_FLUX2KLEIN_自选出图 (1)_2063478532617101314.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `Int` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `TT_img_enc_v2` —— 2/4 个有
- `Text` —— 2/4 个有
- `ZML_SwitchOutput` —— 2/4 个有
- `Get Image Size` —— 1/4 个有
- `OpenposePreprocessor` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/4 个有
- `ResolutionStdSelector` —— 1/4 个有
- `TTResolutionSelector` —— 1/4 个有
- `TwoWaySwitch` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
