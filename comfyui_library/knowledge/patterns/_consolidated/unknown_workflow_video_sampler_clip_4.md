---
name: unknown_workflow_video_sampler_clip_4
type: Unknown Workflow
frequency: 47
level: strong
coverage: 0.993596
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1988225177865641985.json, 视频生成/图生视频/1988615220765614082.json, 视频生成/图生视频/2010681519400034305.json, 视频生成/图生视频/2010685472720293889.json, 视频生成/图生视频/2022695348518522881.json, 视频生成/图生视频/2059832130892550145.json, 视频生成/图生视频/2063803655928766465.json, 视频生成/图生视频/2069687401794064385.json, 视频生成/图生视频/2010689825397018625.json, 视频生成/图生视频/2015621042139566081.json, 视频生成/图生视频/2022240074083082242.json, 视频生成/图生视频/Wan2.2 V3 丝滑图生视频_2085749492984401922.json, 视频生成/图生视频/2062721995304955905.json, 视频生成/图生视频/2065249355430449154.json, 视频生成/图生视频/2079815036926783490.json, 视频生成/图生视频/2069948669922725889.json, 视频生成/图生视频/2067127953313583105.json, 视频生成/图生视频/2079386376218435585.json, 视频生成/图生视频/Wan2.2_Remix_V3_图生视频超流畅最强版_2101853750293000193.json, 视频生成/图生视频/Wan2.2_Remix_V3_图生视频超流畅最强版_2102664220360929281.json, 视频生成/图生视频/Wan2.2_Remix_V3_图生视频超流畅最强版_2102964268558798849.json, 视频生成/图生视频/Wan2.2_Remix_V3_图生视频超流畅最强版_2110571382307385346.json, 视频生成/图生视频/Wan2.2_Remix_V3_图生视频超流畅最强版_2111012816948912129.json, 视频生成/图生视频/2066695652163284993.json, 视频生成/图生视频/优化版 Wan2.2 Remix V3 图生视频_2087918295860203522.json, 视频生成/图生视频/2062010063329521666.json, 视频生成/图生视频/2072567519474438146.json, 视频生成/图生视频/2075050765437198338.json, 视频生成/图生视频/2066688919793655810.json, 视频生成/图生视频/2072513717627088897.json, 视频生成/图生视频/2072515754112667650.json, 视频生成/图生视频/2073603689817919489.json, 视频生成/图生视频/2062050188516220930.json, 视频生成/图生视频/2068616634474000385.json, 视频生成/图生视频/图生视频_2108414096944222209.json, 视频生成/图生视频/2075461259432124418.json, 视频生成/图生视频/图生视频超流畅最强版Wan2.2+Remix+V3+_2083825723554492418.json, 视频生成/图生视频/2064427317950246914.json, 视频生成/图生视频/2075490820677001218.json, 视频生成/图生视频/2066038287848001538.json, 视频生成/图生视频/2065021049787469825.json, 视频生成/文生视频/Wan2.2 Remix V3 图生视频_2064528430519115778.json, 视频生成/文生视频/Wan2.2 Remix V3 图生视频_2064548764462964737.json, 视频生成/文生视频/Wan2.2 Remix V3 图生视频_2070034805030477826.json, 视频生成/文生视频/Wan2.2 Remix V3 图生视频超流畅最强版_2095030298126929921.json, 视频生成/文生视频/Wan2.2 Remix V3 图生视频超流畅最强版_2095807107621801985.json, 视频生成/文生视频/Wan2.2 Remix V3 图生视频超流畅最强版_2104826544370839553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 47 个 workflow 归纳得出（视频生成/图生视频/1988225177865641985.json、视频生成/图生视频/1988615220765614082.json、视频生成/图生视频/2010681519400034305.json、视频生成/图生视频/2010685472720293889.json、视频生成/图生视频/2022695348518522881.json…）

- **类型**：Unknown Workflow
- **样本数**：47
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 47 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 45/47 个有
- `LoraLoaderModelOnly` —— 45/47 个有
- `ModelPatchTorchSettings` —— 43/47 个有
- `CLIPVisionEncode` —— 41/47 个有
- `CLIPVisionLoader` —— 41/47 个有
- `CR Text` —— 40/47 个有
- `Text Concatenate` —— 38/47 个有
- `Wan22PromptSelector` —— 38/47 个有
- `WanImageToVideo` —— 37/47 个有
- `ImageScaleBy` —— 36/47 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 36/47 个有
- `RIFE VFI` —— 36/47 个有
- `easy cleanGpuUsed` —— 36/47 个有
- `ImageResizeKJv2` —— 11/47 个有
- `WanFirstMiddleLastFrameToVideo` —— 7/47 个有
- `ImpactInt` —— 2/47 个有
- `WanFirstLastFrameToVideo` —— 2/47 个有
- `WanVideoNAG` —— 2/47 个有
- `EmptyImage` —— 1/47 个有
- `GetNode` —— 1/47 个有
- `ImageResizeKJ` —— 1/47 个有
- `PainterI2V` —— 1/47 个有
- `PreviewImage` —— 1/47 个有
- `SetNode` —— 1/47 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 47 | 98% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 47 | 93% |
| 采样算法 | 1 | 1 - 1 | 47 | 100% |
| 调度器 | euler | - | 47 | 98% |
| 重绘幅度 | simple | - | 47 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，47 个样本，一致性 98%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，47 个样本，取值集中（一致性 93%）
- 采样算法 中位数 1，观测区间 1 - 1，47 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，47 个样本，一致性 98%
- 重绘幅度 最常用 simple，47 个样本，一致性 91%
