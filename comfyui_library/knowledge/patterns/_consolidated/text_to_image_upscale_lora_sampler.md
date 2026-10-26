---
name: text_to_image_upscale_lora_sampler
type: Text To Image
frequency: 23
level: strong
coverage: 0.843348
common_nodes: [CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/SD教程专用-图像+三视图_2035383250163605506.json, 图片生成/文生图/Z Image Base _ Kook__如梦似幻_2053800942981664769.json, 图片生成/文生图/Z-Image-Turbo瑶光-超真实增强版_2067510090214760449.json, 图片生成/文生图/Z-Image-出人设图_2051158160467087361.json, 图片生成/文生图/Z-Image-出人设图_超真实细节增强_2038461745076899841.json, 图片生成/文生图/Z-Image-文生图-超真实细节增强_2064964807132008450.json, 图片生成/文生图/Z-Image-文生图-超真实细节增强_2065333042721411074.json, 图片生成/文生图/Z-Image-瑶光+超现实3.0-人设图v2.0_2044973775908769794.json, 图片生成/文生图/Z-Image-瑶光版-超真实细节_2082340410323726337.json, 图片生成/文生图/Z-Image-瑶光版-超真实细节增强+4K放大_2056677168402489346.json, 图片生成/文生图/Z-Image-瑶光版-超真实细节增强-人物四视图_2094975538946461697.json, 图片生成/文生图/Z-Image-瑶光版-超真实细节增强-邻家AI大女孩_2043199429162831874.json, 图片生成/文生图/Z-Image-瑶光版-超真实细节增强_2034887394511556610.json, 图片生成/文生图/Z-Image-真实细节增强_2046912552923303937.json, 图片生成/文生图/Z-Image-空姐模特_2066181843638349824.json, 图片生成/文生图/Z-Image-超真实细节增强_2036059631230918657.json, 图片生成/文生图/Z-Image短剧拍档支持场景和角色_2055879009824722945.json, 图片生成/文生图/Z-image-base 自动提示词润色生成真实人像 - 4K_2039950346277097473.json, 图片生成/文生图/Z-image文生图批量工作流直出4K（动漫短剧资产生图抽卡专用）_2102674578551164929.json, 图片生成/文生图/ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2059586906224156674.json, 图片生成/文生图/ZImage+Kook瑶光lora真实人像工作流_2042132652228087809.json, 图片生成/文生图/z_image 角色资产制作+如梦似幻 超绝美感+SEEDVR2放大_2112395440854487041.json, 图片生成/文生图/全能图片B2：生成角色图像三视图工作流_2035677159926276097.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/文生图/SD教程专用-图像+三视图_2035383250163605506.json、图片生成/文生图/Z Image Base _ Kook__如梦似幻_2053800942981664769.json、图片生成/文生图/Z-Image-Turbo瑶光-超真实增强版_2067510090214760449.json、图片生成/文生图/Z-Image-出人设图_2051158160467087361.json、图片生成/文生图/Z-Image-出人设图_超真实细节增强_2038461745076899841.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 22/23 个有
- `CR Text` —— 21/23 个有
- `Fast Groups Bypasser (rgthree)` —— 21/23 个有
- `PreviewImage` —— 21/23 个有
- `INTConstant` —— 20/23 个有
- `FastFilmGrain` —— 18/23 个有
- `LayerColor: BrightnessContrastV2` —— 18/23 个有
- `LoadImage` —— 3/23 个有
- `MuyeTextEditOutput` —— 2/23 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 2/23 个有
- `CLIPLoaderGGUF` —— 1/23 个有
- `CompressImages` —— 1/23 个有
- `HAIGC_SaveImagesToZip` —— 1/23 个有
- `LayerUtility: TextJoin` —— 1/23 个有
- `RH_LLMAPI_Pro_Node` —— 1/23 个有
- `easy showAnything` —— 1/23 个有
- `孤海注释` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 23 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 23 | 100% |
| 采样算法 | res_2s | - | 23 | 78% |
| 调度器 | bong_tangent | - | 23 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |
| 宽度 | 1080 | 1080 - 1920 | 23 | 73% |
| 高度 | 1920 | 1080 - 1920 | 23 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，23 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，23 个样本，一致性 78%
- 调度器 最常用 bong_tangent，23 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1920，23 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，23 个样本，取值集中（一致性 80%）
- 高发问题（23/23 个样本）：Steps较低可能导致细节不足
