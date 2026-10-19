---
name: unknown_workflow_video_upscale_latent_upscale_5
type: Unknown Workflow
frequency: 30
level: strong
coverage: 0.9251
common_nodes: [AnyBooleanSwitch, CFGGuider, CLIPTextEncode, CR Text, DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageResizeKJv2, ImageScaleBy, ImageScaleToTotalPixels, ImpactConditionalBranch, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, ShowText|pysssss, SimpleMath+, UNETLoader, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy anythingIndexSwitch, easy boolean, easy getNode, easy int, easy seed, easy setNode, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/2071400203843887105.json, 视频生成/图生视频/2063510124647501826.json, 视频生成/图生视频/2067966236385955842.json, 视频生成/图生视频/2063514992204402689.json, 视频生成/图生视频/2063657847392653313.json, 视频生成/图生视频/2068269572532301826.json, 视频生成/图生视频/2069446019338825729.json, 视频生成/图生视频/2069450456006479874.json, 视频生成/图生视频/2070162122436341762.json, 视频生成/图生视频/2063508578169868290.json, 视频生成/图生视频/2066799541390757889.json, 视频生成/图生视频/2057441075236786177.json, 视频生成/图生视频/2057453427411734529.json, 视频生成/图生视频/2057457317876158465.json, 视频生成/图生视频/2059892222568517633.json, 视频生成/图生视频/2062564997997350914.json, 视频生成/图生视频/2078533389237444610.json, 视频生成/图生视频/2049604629536710658.json, 视频生成/图生视频/2073419735643021314.json, 视频生成/图生视频/2075248716268793858.json, 视频生成/图生视频/2058740968471490562.json, 视频生成/图生视频/2066695460735246338.json, 视频生成/图生视频/2057276189835878401.json, 视频生成/图生视频/2064146119717900289.json, 视频生成/图生视频/2068941546032029697.json, 视频生成/图生视频/2068056046203133953.json, 视频生成/图生视频/LTX2.6  1080P 50帧率图生视频_2D动漫循环动态壁纸_2089894207166173185.json, 视频生成/图生视频/2063185673980563457.json, 视频生成/图生视频/2057730859171663873.json, 视频生成/图生视频/2058710235518427137.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_5

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（视频生成/图生视频/2071400203843887105.json、视频生成/图生视频/2063510124647501826.json、视频生成/图生视频/2067966236385955842.json、视频生成/图生视频/2063514992204402689.json、视频生成/图生视频/2063657847392653313.json…）

- **类型**：Unknown Workflow
- **样本数**：30
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 30 个 workflow 都包含：
- `AnyBooleanSwitch`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImpactConditionalBranch`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplaceKJ`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `SimpleMath+`
- `UNETLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `easy boolean`
- `easy getNode`
- `easy int`
- `easy seed`
- `easy setNode`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `LTXVTiledVAEDecode` —— 25/30 个有
- `PrimitiveFloat` —— 25/30 个有
- `SetReserveVRAM` —— 25/30 个有
- `CM_BoolToInt` —— 5/30 个有
- `CM_IntToFloat` —— 5/30 个有
- `VAEDecode` —— 5/30 个有
- `DuckHideNode` —— 1/30 个有
- `SaveImage` —— 1/30 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 30 | 100% |
| 高度 | 25 | 25 - 25 | 30 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，30 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，30 个样本，取值集中（一致性 100%）
