---
name: unknown_workflow_sampler_clip_unet_17
type: Unknown Workflow
frequency: 28
level: moderate
coverage: 0.932321
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 一键转毛线风格_1996554829826760706.json, 图片生成/图生图/Flux2 单图编辑_1993555111395917826.json, 图片生成/图生图/Flux2 单图编辑模式_1993596098176548866.json, 图片生成/图生图/Flux2 双图编辑_1993555181015154690.json, 图片生成/图生图/Flux2 图片编辑_1986702252859666433.json, 图片生成/图生图/Flux2 超强双图编辑_1993619885911638017.json, 图片生成/图生图/Flux2-klein-9b 多图编辑_2016048290185351169.json, 图片生成/图生图/Flux2.klein单图编辑（去水印_换背景_改色）_2013100887060779010.json, 图片生成/图生图/Flux2DEV单图编辑_1993536804617912321.json, 图片生成/图生图/Flux2DEV单图编辑_1994060590549319682.json, 图片生成/图生图/Flux2DEV多图编辑_1993572546985607169.json, 图片生成/图生图/Flux2_多图编辑工作流_1994701624062906369.json, 图片生成/图生图/Flux2一键3D毛线质感（超还原）_2028277318543740929.json, 图片生成/图生图/Flux2万物转毛线风格=B站艾橘溪_1986842346891456514.json, 图片生成/图生图/Flux2万物转毛线风格_2015686369653297154.json, 图片生成/图生图/Flux2万物转毛线风格_2036267536605515778.json, 图片生成/图生图/Flux2万物转毛线风格_2067131882885697537.json, 图片生成/图生图/Flux2万物转毛线风格_2067134254907224066.json, 图片生成/图生图/Flux2万物转毛线风格画风_2068870823557033986.json, 图片生成/图生图/Flux2三图编辑_1993501566938398721.json, 图片生成/图生图/Flux2单图编辑_1993496482062024706.json, 图片生成/图生图/Flux2双图编辑_1993496664094818306.json, 图片生成/图生图/Flux2变毛线_1996852914805252098.json, 图片生成/图生图/flux2 人物换装_电商产品换背景_2049895408285044737.json, 图片生成/图生图/flux2klein9b自动溶图重新打光_2046941528681095169.json, 图片生成/图生图/klein溶图打光_2110918582837272578.json, 图片生成/图生图/上传图片即可一键把角色变成毛线材质，Flux2万物转毛线风格_2026105296489291777.json, 图片生成/图生图/上传图片即可一键把角色变成毛线材质，Flux2万物转毛线风格_2052921408677785602.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_17

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/图生图/Flux2 一键转毛线风格_1996554829826760706.json、图片生成/图生图/Flux2 单图编辑_1993555111395917826.json、图片生成/图生图/Flux2 单图编辑模式_1993596098176548866.json、图片生成/图生图/Flux2 双图编辑_1993555181015154690.json、图片生成/图生图/Flux2 图片编辑_1986702252859666433.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 28 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `EmptyFlux2LatentImage` —— 26/28 个有
- `FluxGuidance` —— 26/28 个有
- `PrimitiveInt` —— 18/28 个有
- `ImageScaleToTotalPixels` —— 14/28 个有
- `GetImageSizeAndCount` —— 11/28 个有
- `ImageScaleDownToSize` —— 11/28 个有
- `LayerUtility: PurgeVRAM` —— 11/28 个有
- `Image Stitch` —— 10/28 个有
- `CR Prompt Text` —— 6/28 个有
- `Int` —— 6/28 个有
- `Image Comparer (rgthree)` —— 4/28 个有
- `GetImageSize` —— 3/28 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/28 个有
- `LoraLoaderModelOnly` —— 2/28 个有
- `easy positive` —— 2/28 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
