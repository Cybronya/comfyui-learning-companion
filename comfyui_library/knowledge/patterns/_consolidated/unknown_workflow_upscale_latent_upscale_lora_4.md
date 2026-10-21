---
name: unknown_workflow_upscale_latent_upscale_lora_4
type: Unknown Workflow
frequency: 47
level: strong
coverage: 0.924106
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2017478785842548737.json, 视频生成/图生视频/2014309275279036418.json, 视频生成/图生视频/2079136882214137857.json, 视频生成/图生视频/2079979154077995009.json, 视频生成/图生视频/2080341999642824705.json, 视频生成/图生视频/2080563704462135297.json, 视频生成/图生视频/2082330133825937409.json, 视频生成/图生视频/图生视频  视频生成  LTX2.3 最强开源_2084153840399634434.json, 视频生成/图生视频/2077299088692961282.json, 视频生成/图生视频/图生视频  视频生成  视频   LTX2.3  最强开源_2083480109931126786.json, 视频生成/图生视频/2077297200933195777.json, 视频生成/图生视频/2077314201252618241.json, 视频生成/图生视频/2077352906352848897.json, 视频生成/图生视频/2079987879677353986.json, 视频生成/图生视频/2081669323676020738.json, 视频生成/图生视频/图生视频  视频生成  视频   LTX2.3 最强开源_2082762135133839362.json, 视频生成/图生视频/图生视频  视频生成  视频   LTX2.3 最强开源_2083125386006851585.json, 视频生成/图生视频/2046500651789717505.json, 视频生成/图生视频/2046846957221580801.json, 视频生成/图生视频/2031014725928095745.json, 视频生成/图生视频/2046417556843536386.json, 视频生成/图生视频/2047143040543887362.json, 视频生成/图生视频/2047131177831636994.json, 视频生成/图生视频/2047205573208313857.json, 视频生成/图生视频/2057285774952980482.json, 视频生成/图生视频/2079077960786735105.json, 视频生成/图生视频/2082269605258682369.json, 视频生成/图生视频/2047479743863332865.json, 视频生成/图生视频/2046138423576104961.json, 视频生成/图生视频/2064698112870010881.json, 视频生成/图生视频/2068335067583307778.json, 视频生成/图生视频/2076613090795413506.json, 视频生成/图生视频/2077007300753182722.json, 视频生成/图生视频/视频生成  LTX2.3 图生视频 最强开源_2082716206850727937.json, 视频生成/图生视频/2079495472238129153.json, 视频生成/图生视频/2080734800876490753.json, 视频生成/图生视频/视频生成  视频   LTX2.3 图生视频 最强开源_2082761804425555970.json, 视频生成/图生视频/视频生成  视频   LTX2.3 图生视频 最强开源_2083263132746731521.json, 视频生成/图生视频/视频生成  视频   LTX2.3 图生视频 最强开源_2083951843780161538.json, 视频生成/图生视频/视频生成  视频   LTX2.3 图生视频 最强开源_2084169351942463489.json, 视频生成/图生视频/2078761295033225218.json, 视频生成/图生视频/2073934539000475650.json, 视频生成/图生视频/2073938374595010562.json, 视频生成/图生视频/2075025699286634498.json, 视频生成/图生视频/2074378391851192322.json, 视频生成/图生视频/2074389452264398849.json, 视频生成/文生视频/CG少女风格文生视频_图生视频2合1自由切换版-LTX2.3_2038339473397784578.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 47 个 workflow 归纳得出（视频生成/图生视频/2017478785842548737.json、视频生成/图生视频/2014309275279036418.json、视频生成/图生视频/2079136882214137857.json、视频生成/图生视频/2079979154077995009.json、视频生成/图生视频/2080341999642824705.json…）

- **类型**：Unknown Workflow
- **样本数**：47
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 47 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
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
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoInplace` —— 46/47 个有
- `PrimitiveInt` —— 46/47 个有
- `KSampler` —— 44/47 个有
- `ResizeImageMaskNode` —— 44/47 个有
- `DualCLIPLoader` —— 43/47 个有
- `TextGenerateLTX2Prompt` —— 43/47 个有
- `CreateVideo` —— 39/47 个有
- `SaveVideo` —— 39/47 个有
- `PreviewAny` —— 35/47 个有
- `SetNode` —— 16/47 个有
- `GetNode` —— 15/47 个有
- `VHS_VideoCombine` —— 9/47 个有
- `ImageResizeKJv2` —— 8/47 个有
- `Text` —— 8/47 个有
- `DF_Int_to_Float` —— 6/47 个有
- `Int` —— 6/47 个有
- `SimpleMath+` —— 6/47 个有
- `ManualSigmas` —— 4/47 个有
- `PreviewImage` —— 2/47 个有
- `BasicScheduler` —— 1/47 个有
- `BetaSamplingScheduler` —— 1/47 个有
- `INTConstant` —— 1/47 个有
- `LTX2SamplingPreviewOverride` —— 1/47 个有
- `LTX2_NAG` —— 1/47 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/47 个有
- `MemoryCleaner` —— 1/47 个有
- `PrimitiveBoolean` —— 1/47 个有
- `SaveImage` —— 1/47 个有
- `easy cleanGpuUsed` —— 1/47 个有
- `easy seed` —— 1/47 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 47 | 100% |
| 高度 | 25 | 25 - 25 | 47 | 100% |
| 采样步数 | 4 | 4 - 4 | 44 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 44 | 100% |
| 采样算法 | euler | - | 44 | 100% |
| 调度器 | simple | - | 44 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.35 | 44 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 44/47 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，47 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，47 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，44 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，44 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，44 个样本，一致性 100%
- 调度器 最常用 simple，44 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.35，44 个样本，取值集中（一致性 100%）
- 高发问题（44/47 个样本）：Steps较低可能导致细节不足
