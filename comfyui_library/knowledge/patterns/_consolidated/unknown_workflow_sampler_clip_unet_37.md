---
name: unknown_workflow_sampler_clip_unet_37
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.929056
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein 商业级人像精修｜超强一致性_2085535726921404417.json, 图片生成/图生图/Flux2 Klein_转精致3D建模风格_2041871546448351234.json, 图片生成/图生图/Flux2 Klein_转精致3D建模风格_2042590574431182849.json, 图片生成/图生图/Flux2 Klein｜1 图像编辑（终极版V3：角色一致性，保留角色全身特征）_2052041548086427649.json, 图片生成/图生图/Flux2 Sun Direction LoRA 精确控制‌图片光影_2087880030058795010.json, 图片生成/图生图/Flux2 klein 单图编辑_2062060544747728897.json, 图片生成/图生图/Flux2 klein 双图编辑_2062063724688658433.json, 图片生成/图生图/Flux2 klein 图生图+高清放大_2062043788545191938.json, 图片生成/图生图/Flux2 klein 多图编辑_2062073276687540225.json, 图片生成/图生图/Flux2+Klein9b全能图像编辑：超强一致性全能图像模型_2031926623477436417.json, 图片生成/图生图/Flux2Klein9b万物迁移_2065953597262749698.json, 图片生成/图生图/Flux2_Klein_商业级人像精修｜超强一致性_2085908338545614849.json, 图片生成/图生图/Flux2_Klein_商业级人像精修｜超强一致性_2085926483779997698.json, 图片生成/图生图/Flux2_Sun_Direction_LoRA_精确控制‌图片光影_2091354005774622721.json, 图片生成/图生图/Flux2_Sun_Direction_LoRA_精确控制‌图片光影_2091821134911201281.json, 图片生成/图生图/Flux2_Sun_Direction_LoRA_精确控制‌图片光影_2092610607378944002.json, 图片生成/图生图/Flux2_klein_图生图+高清放大_2072851483212734466.json, 视频生成/图生视频/Flux2_klein_图生图+高清放大_2072586147523551233.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_37

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 商业级人像精修｜超强一致性_2085535726921404417.json、图片生成/图生图/Flux2 Klein_转精致3D建模风格_2041871546448351234.json、图片生成/图生图/Flux2 Klein_转精致3D建模风格_2042590574431182849.json、图片生成/图生图/Flux2 Klein｜1 图像编辑（终极版V3：角色一致性，保留角色全身特征）_2052041548086427649.json、图片生成/图生图/Flux2 Sun Direction LoRA 精确控制‌图片光影_2087880030058795010.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 18 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
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
- `EmptyFlux2LatentImage` —— 15/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 15/18 个有
- `GetImageSize` —— 13/18 个有
- `Image Comparer (rgthree)` —— 12/18 个有
- `CR Text` —— 10/18 个有
- `LoraLoaderModelOnly` —— 10/18 个有
- `ImageScaleToTotalPixels` —— 8/18 个有
- `SeedVR2LoadDiTModel` —— 8/18 个有
- `SeedVR2LoadVAEModel` —— 8/18 个有
- `SeedVR2VideoUpscaler` —— 8/18 个有
- `Anything Everywhere` —— 6/18 个有
- `easy int` —— 5/18 个有
- `SphereLightNode` —— 4/18 个有
- `GetImageSize+` —— 3/18 个有
- `Int` —— 3/18 个有
- `Fast Groups Muter (rgthree)` —— 2/18 个有
- `HAIGC_SavePSD` —— 1/18 个有
- `IdentityFeatureTransferV3` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
