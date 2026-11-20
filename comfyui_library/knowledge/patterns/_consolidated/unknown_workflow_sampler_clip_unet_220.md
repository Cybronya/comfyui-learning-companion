---
name: unknown_workflow_sampler_clip_unet_220
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.960143
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/根据参考图修改图片_2016313387927478274.json, 图片生成/图生图/漫反射图案提取（klein2）_2077593751765209090.json, 平台全量/Klein-9B换背景_2088838297077510145.json, 平台全量/优化皮肤真实感 极致真实Flux2-Klein9b 图片变清晰去AI油腻 高清放大 增加细节 去除A_2045664372873240577.json, 平台全量/优化皮肤真实感 极致真实Flux2-Klein9b 图片放在变清晰去AI油腻 高清放大 增加细节 去_2022832692991107073.json, 平台全量/增加细节+高清放大  去除AI塑料感 Flux2 Klein 优化皮肤 渲染现实_2026485821662044161.json, 平台全量/星绘-自动COS修图（Automatic COS photo editing）_2022573412341784578.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_220

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/根据参考图修改图片_2016313387927478274.json、图片生成/图生图/漫反射图案提取（klein2）_2077593751765209090.json、平台全量/Klein-9B换背景_2088838297077510145.json、平台全量/优化皮肤真实感 极致真实Flux2-Klein9b 图片变清晰去AI油腻 高清放大 增加细节 去除A_2045664372873240577.json、平台全量/优化皮肤真实感 极致真实Flux2-Klein9b 图片放在变清晰去AI油腻 高清放大 增加细节 去_2022832692991107073.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `DifferentialDiffusion` —— 4/7 个有
- `GrowMaskWithBlur` —— 4/7 个有
- `GetImageSize` —— 3/7 个有
- `1hew_TextListToString` —— 1/7 个有
- `CR Text Concatenate` —— 1/7 个有
- `DF_String_Concatenate` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `PurgeVRAM_UTK` —— 1/7 个有
- `Qwen3_VQA` —— 1/7 个有
- `TextToLowercase` —— 1/7 个有
- `easy imageScaleDownToSize` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
