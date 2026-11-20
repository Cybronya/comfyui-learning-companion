---
name: unknown_workflow_sampler_clip_unet_137
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.940556
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图生图海报1_2021770523801292801.json, 图片生成/图生图/多图编辑 Flux2-Klein-9b_2062081939934367746.json, 图片生成/图生图/多图编辑 Flux2-Klein_1979531857857515522.json, 图片生成/图生图/生产力-flux2_klein单图+多图参考_2013052924347289602.json, 图片生成/图生图/真人转赛璐璐风格编辑_2068932411035045890.json, 图片生成/图生图/线稿_2016078729386139649.json, 图片生成/图生图/设计工作流——双图迁移_2013146117600448514.json, 图片生成/文生图/文生图+图生图_2039179127982399489.json, 图片生成/文生图/文生图+图生图_2044754006899171330.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_137

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/图生图海报1_2021770523801292801.json、图片生成/图生图/多图编辑 Flux2-Klein-9b_2062081939934367746.json、图片生成/图生图/多图编辑 Flux2-Klein_1979531857857515522.json、图片生成/图生图/生产力-flux2_klein单图+多图参考_2013052924347289602.json、图片生成/图生图/真人转赛璐璐风格编辑_2068932411035045890.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/9 个有
- `ImageScaleToTotalPixels` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `GetImageSize` —— 6/9 个有
- `SaveImage` —— 6/9 个有
- `Text` —— 5/9 个有
- `Image Comparer (rgthree)` —— 4/9 个有
- `CR Text` —— 3/9 个有
- `CompressImages` —— 3/9 个有
- `DoubaoSizePreset` —— 3/9 个有
- `PlaySound|pysssss` —— 3/9 个有
- `SaveImagePlus` —— 3/9 个有
- `AILab_QwenVL_Advanced` —— 1/9 个有
- `CR Text Concatenate` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `ImageConcanate` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `Seed (rgthree)` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
