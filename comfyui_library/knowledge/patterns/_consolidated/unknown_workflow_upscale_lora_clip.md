---
name: unknown_workflow_upscale_lora_clip
type: Unknown Workflow
frequency: 23
level: strong
coverage: 0.804783
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, Image Comparer (rgthree), ImageScaleBy, Lora Loader, PrimitiveFloat, RHHiddenNodes, RH_Translator, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/AI生成韩系氛围感写真_高级感大片_2059080719774871553.json, 图片生成/文生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2068534967176622081.json, 图片生成/文生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2072158202266996738.json, 图片生成/文生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2072954583877509121.json, 图片生成/文生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2073598216662245377.json, 图片生成/文生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2074754185714819074.json, 图片生成/文生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2077820349277892609.json, 图片生成/文生图/FLUX.1AI生成韩系氛围感写真_高级感大片图片生成_2073287149864181762.json, 图片生成/文生图/FLUX.1AI生成韩系氛围感写真_高级感大片图片生成_2073304134752751618.json, 图片生成/文生图/一键美图生成_2060281505628377090.json, 图片生成/文生图/洗图 文生图 人像写真 +SeedVR2高清放大 美图生成-抖音快手小红书_2059461117663076353.json, 图片生成/文生图/洗图 文生图 人像写真 +SeedVR2高清放大 美图生成_2060302391127404546.json, 图片生成/文生图/洗图 文生图 人像写真 +SeedVR2高清放大 美图生成_2064685682345472002.json, 图片生成/文生图/洗图 文生图 人像写真 +SeedVR2高清放大 美图生成_2072194512797134849.json, 图片生成/文生图/美图生成-抖音快手小红书V2.0_2061273916148117505.json, 图片生成/文生图/美图生成-抖音快手小红书_2029537281849171969.json, 图片生成/文生图/美图生成-抖音快手小红书_2061270943720370177.json, 图片生成/文生图/美图生成-抖音快手小红书_2061613051719282690.json, 图片生成/文生图/美图生成-抖音快手小红书专属_2064637395596832770.json, 图片生成/文生图/美图生成-文生视频_2060280767871283201.json, 图片生成/文生图/美图生成器_2060179705269145601.json, 图片生成/文生图/高清放大-美图生成-抖音快手小红书_2059478502654697473.json, 视频生成/图生视频/2075039928815284225.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_clip

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/文生图/AI生成韩系氛围感写真_高级感大片_2059080719774871553.json、图片生成/文生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2068534967176622081.json、图片生成/文生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2072158202266996738.json、图片生成/文生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2072954583877509121.json、图片生成/文生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2073598216662245377.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `Lora Loader`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `RH_Translator`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/23 个有
- `LoadImage` —— 4/23 个有
- `PreviewAny` —— 4/23 个有
- `RH_Captioner` —— 4/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 23 | 100% |
| 高度 | 1920 | 1920 - 1920 | 23 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，23 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，23 个样本，取值集中（一致性 100%）
