---
name: unknown_workflow_sampler_clip_unet_55
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.839437
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/ltx-2.5-22b-ic-lora-ingredients-0.9 参考图 Lora 视频工作流_2110025875143086082.json, 平台全量/LTX-2.5 Alpha-Gen 视频抠像工作流_2110324826882793474.json, 平台全量/LTX-2.5 Day-To-Night Lora 昼夜转换工作流_2110236700088815618.json, 平台全量/LTX-2.5 Deblur Lora 视频去模糊（失焦修复）工作流_2110303433403228162.json, 平台全量/LTX-2.5 Decompression Lora 视频去伪影工作流_2110273535066333185.json, 平台全量/LTX-2.5 Restore Lora 历史影像修复工作流_2110313044113969154.json, 平台全量/LTX-2.5 Water Lora 视频到视频 水特效添加工作流_2110249425766535170.json, 平台全量/LTX-2.5 视频双效修复-智能着色与去伪影工作流_2110332087919276033.json, 平台全量/LTX-2.5-22b-IC-LoRA-Clean-Plate 视频对象清除工作流_2110229913277132802.json, 平台全量/LTX2.5-Colorization 色彩修复Lora 视频到视频工作流_2110045122980302849.json, 平台全量/LTX2.5-Refine-Details 视频细节精修工作流_2110321013971054594.json, 视频生成/图生视频/LTX-2.5 Cinemagraph 局部动态 图像到视频 ComfyUI 工作流_2110222043215130625.json, 视频生成/图生视频/LTX-2.5 Slow Motion Control 慢动作视频生成工作流_2110054667488153602.json, 视频生成/图生视频/LTX-2.5 单图多参_2087502470892310529.json, 视频生成/图生视频/LTX2.5图生视频 -高质量直出1K_2087559276465319937.json, 视频生成/文生视频/LTX2.5_I2V_T2V_2087347078044405762.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_55

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/ltx-2.5-22b-ic-lora-ingredients-0.9 参考图 Lora 视频工作流_2110025875143086082.json、平台全量/LTX-2.5 Alpha-Gen 视频抠像工作流_2110324826882793474.json、平台全量/LTX-2.5 Day-To-Night Lora 昼夜转换工作流_2110236700088815618.json、平台全量/LTX-2.5 Deblur Lora 视频去模糊（失焦修复）工作流_2110303433403228162.json、平台全量/LTX-2.5 Decompression Lora 视频去伪影工作流_2110273535066333185.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 14/16 个有
- `PrimitiveFloat` —— 14/16 个有
- `CFGGuider` —— 13/16 个有
- `LTXAddVideoICLoRAGuide` —— 12/16 个有
- `LTXICLoRALoaderModelOnly` —— 12/16 个有
- `LTXVCropGuides` —— 12/16 个有
- `XB_CanvasLabel` —— 12/16 个有
- `GetVideoComponents` —— 11/16 个有
- `ImageScale` —— 11/16 个有
- `ImageFromBatch` —— 10/16 个有
- `LoadVideo` —— 10/16 个有
- `Video Slice` —— 10/16 个有
- `LTXVAudioVAEDecode` —— 6/16 个有
- `LoadImage` —— 6/16 个有
- `LTXVImgToVideoInplace` —— 5/16 个有
- `LTXVPreprocess` —— 5/16 个有
- `ResizeImageMaskNode` —— 5/16 个有
- `LTXVDualCFGGuider` —— 3/16 个有
- `LTXVLatentUpsampler` —— 3/16 个有
- `LatentUpscaleModelLoader` —— 3/16 个有
- `PrimitiveBoolean` —— 3/16 个有
- `LoraLoaderModelOnly` —— 2/16 个有
- `RepeatImageBatch` —— 2/16 个有
- `ResolutionSelector` —— 2/16 个有
- `Label (rgthree)` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 16 | 94% |
| 高度 | 25 | 24 - 25 | 16 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，16 个样本，取值集中（一致性 94%）
- 高度 中位数 25，观测区间 24 - 25，16 个样本，取值集中（一致性 99%）
