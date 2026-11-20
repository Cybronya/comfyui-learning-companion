---
name: unknown_workflow_sampler_clip_unet_26
type: Unknown Workflow
frequency: 22
level: moderate
coverage: 0.926
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein 商业级人像精修｜超强一致性_2085535726921404417.json, 图片生成/图生图/Flux2 Klein_转精致3D建模风格_2041871546448351234.json, 图片生成/图生图/Flux2 Klein_转精致3D建模风格_2042590574431182849.json, 图片生成/图生图/Flux2 Klein｜1 图像编辑（终极版V3：角色一致性，保留角色全身特征）_2052041548086427649.json, 图片生成/图生图/Flux2 Sun Direction LoRA 精确控制‌图片光影_2087880030058795010.json, 图片生成/图生图/Flux2 klein 单图编辑_2062060544747728897.json, 图片生成/图生图/Flux2 klein 双图编辑_2062063724688658433.json, 图片生成/图生图/Flux2 klein 图生图+高清放大_2062043788545191938.json, 图片生成/图生图/Flux2 klein 多图编辑_2062073276687540225.json, 图片生成/图生图/Flux2+Klein9b全能图像编辑：超强一致性全能图像模型_2031926623477436417.json, 图片生成/图生图/Flux2Klein9b万物迁移_2065953597262749698.json, 图片生成/图生图/Flux2_Klein_商业级人像精修｜超强一致性_2085908338545614849.json, 图片生成/图生图/Flux2_Klein_商业级人像精修｜超强一致性_2085926483779997698.json, 图片生成/图生图/Flux2_Sun_Direction_LoRA_精确控制‌图片光影_2091354005774622721.json, 图片生成/图生图/Flux2_Sun_Direction_LoRA_精确控制‌图片光影_2091821134911201281.json, 图片生成/图生图/Flux2_Sun_Direction_LoRA_精确控制‌图片光影_2092610607378944002.json, 图片生成/图生图/Flux2_klein_图生图+高清放大_2072851483212734466.json, 图片生成/图生图/Klein细节修复+SeedVR2图像放大_2031519082889093121.json, 图片生成/图生图/Klein细节修复+SeedVR2图像放大_2116710198713872385.json, 图片生成/图生图/Klein细节修复+SeedVR2图像放大_2116724754924265473.json, "图片生成/图生图/电商神器flux-2-klein+SeedVR2细节增强+4倍放大模型,适用人物皮肤服饰面料纹理_2034815871520083969.json", "图片生成/图生图/电商神器flux-2-klein+SeedVR2细节增强+4倍放大模型,适用人物皮肤服饰面料纹理_2037006862268239874.json"]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_26

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 商业级人像精修｜超强一致性_2085535726921404417.json、图片生成/图生图/Flux2 Klein_转精致3D建模风格_2041871546448351234.json、图片生成/图生图/Flux2 Klein_转精致3D建模风格_2042590574431182849.json、图片生成/图生图/Flux2 Klein｜1 图像编辑（终极版V3：角色一致性，保留角色全身特征）_2052041548086427649.json、图片生成/图生图/Flux2 Sun Direction LoRA 精确控制‌图片光影_2087880030058795010.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 22 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 20/22 个有
- `EmptyFlux2LatentImage` —— 19/22 个有
- `GetImageSize` —— 17/22 个有
- `Image Comparer (rgthree)` —— 17/22 个有
- `LoraLoaderModelOnly` —— 15/22 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 14/22 个有
- `ImageScaleToTotalPixels` —— 13/22 个有
- `SeedVR2LoadDiTModel` —— 12/22 个有
- `SeedVR2LoadVAEModel` —— 12/22 个有
- `SeedVR2VideoUpscaler` —— 12/22 个有
- `CR Text` —— 9/22 个有
- `Anything Everywhere` —— 5/22 个有
- `ColorMatch` —— 5/22 个有
- `ImageSharpen` —— 5/22 个有
- `easy int` —— 5/22 个有
- `SphereLightNode` —— 4/22 个有
- `GetImageSize+` —— 3/22 个有
- `Int` —— 3/22 个有
- `PreviewImage` —— 3/22 个有
- `Fast Groups Muter (rgthree)` —— 2/22 个有
- `MuyeLoadImage` —— 2/22 个有
- `HAIGC_SavePSD` —— 1/22 个有
- `IdentityFeatureTransferV3` —— 1/22 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
