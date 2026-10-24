---
name: text_to_image_lora_sampler_clip_76
type: Text To Image
frequency: 15
level: strong
coverage: 0.8916
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Moss-image局部重绘｜精准圈选区域修改画面细节无损_2112824699423121409.json, 图片生成/图生图/QWEN PANO360全景图生成工作流 360度全景画面直出_2109702845909000193.json, 图片生成/图生图/Qwe Image 2.1多维运镜构图变换｜附控制指南图生图_2110742888882724865.json, 图片生成/图生图/Qwen 2.1一键换脸换人，图生图角色替换人物身份无缝对齐_2112241514712756225.json, 图片生成/图生图/Qwen 2.1改头换面换头术 人物面部精准替换_2104991945562087425.json, 图片生成/图生图/Qwen 2.1改头换面换头术｜图生图精准换脸｜换头不换身效果自然_2104761533778718721.json, 图片生成/图生图/Qwen Image 2.1 Turbo人物角色替换 人物一致性更强_2109408658609238018.json, 图片生成/图生图/Qwen Image 2.1 Turbo人物角色替换 人物一致性更强_2109748589525295106.json, 图片生成/图生图/Qwen Image 2.1 Turbo多图像编辑8步快速出图 高效改图方案_2109334660395393026.json, 图片生成/图生图/Qwen Image 2.1 Turbo多图像编辑8步快速出图 高效改图方案_2109696542016884738.json, 图片生成/图生图/Qwen Image 2.1图片清晰度增强与细节修复V2 画质提升方案_2109180598479835138.json, 图片生成/图生图/Qwen Image 2.1图片清晰度增强与细节修复V2 画质提升方案_2109778326498926594.json, 图片生成/图生图/Qwen Image 2.1图片编辑工作流，简洁高效的图生图处理方案_2105792533245808642.json, 图片生成/图生图/Qwen Image 2.1文生编辑抠图透明图像工作流，图生图图像处理方案_2107196238646042626.json, 图片生成/图生图/Qwen image 2.1文生编辑抠图一体 透明图像处理方案_2110350738932191233.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_76

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Moss-image局部重绘｜精准圈选区域修改画面细节无损_2112824699423121409.json、图片生成/图生图/QWEN PANO360全景图生成工作流 360度全景画面直出_2109702845909000193.json、图片生成/图生图/Qwe Image 2.1多维运镜构图变换｜附控制指南图生图_2110742888882724865.json、图片生成/图生图/Qwen 2.1一键换脸换人，图生图角色替换人物身份无缝对齐_2112241514712756225.json、图片生成/图生图/Qwen 2.1改头换面换头术 人物面部精准替换_2104991945562087425.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImage21` —— 14/15 个有
- `QwenImage21Cache` —— 13/15 个有
- `Image Comparer (rgthree)` —— 9/15 个有
- `CR Text` —— 8/15 个有
- `ComfySwitchNode` —— 7/15 个有
- `ResolutionSelector` —— 7/15 个有
- `easy showAnything` —— 5/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/15 个有
- `QwenPERewriteT8` —— 3/15 个有
- `SaveImageAdvanced` —— 3/15 个有
- `SeedNode` —— 3/15 个有
- `SplitImageWithAlpha` —— 3/15 个有
- `Change Channel Count` —— 2/15 个有
- `Fast Groups Bypasser (rgthree)` —— 2/15 个有
- `PrimitiveBoolean` —— 2/15 个有
- `QwenImagePromptOptimizer` —— 2/15 个有
- `VOSR2ModelLoader` —— 2/15 个有
- `VOSR2Upscale` —— 2/15 个有
- `easy imageSave` —— 2/15 个有
- `InpaintModelConditioning` —— 1/15 个有
- `Int` —— 1/15 个有
- `Mask Fill Holes` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（21/15 个样本）：Steps较低可能导致细节不足
