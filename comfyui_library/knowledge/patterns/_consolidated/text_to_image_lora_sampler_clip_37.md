---
name: text_to_image_lora_sampler_clip_37
type: Text To Image
frequency: 20
level: strong
coverage: 0.8093
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen Image 2.1全功能工作流 文生图编辑反推一体工具_2114105118831505410.json, 图片生成/反推提示词/qwen Image 2.1全功能工作流｜文生图反推提示词图生图_2114006893998989313.json, 图片生成/图生图/Qwen Image 2.1 AI短剧漫剧人物三视图，图生图角色一致性设计工具_2103949584014860290.json, 图片生成/图生图/Qwen Image 2.1万能输入工作流 文生图图生图处理工具_2113338289234202625.json, 图片生成/图生图/Qwen Image 2.1人物换姿势服装模特姿势复刻工作流，服装展示图生图工具_2107565485087870977.json, 图片生成/图生图/Qwen Image 2.1人物换姿势服装模特姿势复刻工作流，服装展示图生图工具_2107938760527798274.json, 图片生成/图生图/Qwen Image 2.1人物换姿势服装模特姿势复刻工作流，服装展示图生图工具_2108332170640187393.json, 图片生成/图生图/Qwen Image 2.1人物换姿势｜服装模特姿势复刻，摆拍角度随心控_2107360567005634561.json, 图片生成/图生图/Qwen Image 2.1图像合集人像写真实图生图处理工具_2102543389462982657.json, 图片生成/图生图/Qwen Image 2.1图像生成二十步大合集，全方位图生图能力覆盖_2102828879642714114.json, 图片生成/图生图/Qwen Image 2.1图像生成大合集，场景换装图生图多场景一站式工具_2103254188389130241.json, 图片生成/图生图/Qwen Image 2.1图像生成大合集｜多场景文生图图生图一站搞定_2113572080506724353.json, 图片生成/图生图/Qwen Image 2.1图像生成大合集｜文生图图生图全都有｜收藏一个够用了_2102628402149806081.json, 图片生成/图生图/Qwen Image 2.1工作流合集图生图处理生成工具_2102495775229046786.json, 图片生成/图生图/Qwen Image 2.1工作流合集文生图图生图处理工具_2102555854674419713.json, 图片生成/图生图/Qwen Image 2.1工作流大合集｜图生图多种玩法一网打尽｜新手必存_2102238523955965954.json, 图片生成/图生图/Qwen Image 2.1洗图反推提示词，图生图图像分析与提示词提取工具_2103236925317537793.json, 图片生成/图生图/Qwen image 2.1图像高清修复 4K超分放大增强_2110244395655188481.json, 图片生成/图生图/Qwen image 2.1图像高清修复 4K超分放大增强_2110370717484273665.json, 图片生成/图生图/Qwen image 2.1高清修复流程，老图一键放大到4K_2110478470630436865.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_37

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1全功能工作流 文生图编辑反推一体工具_2114105118831505410.json、图片生成/反推提示词/qwen Image 2.1全功能工作流｜文生图反推提示词图生图_2114006893998989313.json、图片生成/图生图/Qwen Image 2.1 AI短剧漫剧人物三视图，图生图角色一致性设计工具_2103949584014860290.json、图片生成/图生图/Qwen Image 2.1万能输入工作流 文生图图生图处理工具_2113338289234202625.json、图片生成/图生图/Qwen Image 2.1人物换姿势服装模特姿势复刻工作流，服装展示图生图工具_2107565485087870977.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 19/20 个有
- `PreviewImage` —— 19/20 个有
- `ComfySwitchNode` —— 18/20 个有
- `GetNode` —— 18/20 个有
- `SetNode` —— 18/20 个有
- `Fast Groups Bypasser (rgthree)` —— 17/20 个有
- `Anything Everywhere3` —— 16/20 个有
- `CR Prompt Text` —— 16/20 个有
- `LayerUtility: ImageReel` —— 16/20 个有
- `LayerUtility: ImageReelComposit` —— 16/20 个有
- `TextGenerateLTX2Prompt` —— 14/20 个有
- `PreviewAny` —— 13/20 个有
- `BatchImagesNode` —— 12/20 个有
- `easy setNode` —— 11/20 个有
- `easy showAnything` —— 10/20 个有
- `ShowText|pysssss` —— 9/20 个有
- `ImageResize+` —— 8/20 个有
- `ImageScaleBy` —— 8/20 个有
- `Seed (rgthree)` —— 8/20 个有
- `SeedVR2LoadDiTModel` —— 8/20 个有
- `SeedVR2LoadVAEModel` —— 8/20 个有
- `SeedVR2VideoUpscaler` —— 8/20 个有
- `TTP_Image_Assy` —— 8/20 个有
- `TTP_Image_Tile_Batch` —— 8/20 个有
- `TTP_Tile_image_size` —— 8/20 个有
- `easy imageSize` —— 8/20 个有
- `LayerUtility: PurgeVRAM` —— 7/20 个有
- `CR Text` —— 3/20 个有
- `ImageResizeKJv2` —— 3/20 个有
- `Latent Switch (JPS)` —— 3/20 个有
- `RepeatLatentBatch` —— 2/20 个有
- `llama_cpp_instruct_adv` —— 2/20 个有
- `llama_cpp_model_loader` —— 2/20 个有
- `llama_cpp_parameters` —— 2/20 个有
- `DWPreprocessor` —— 1/20 个有
- `DepthAnythingV2Preprocessor` —— 1/20 个有
- `LineArtPreprocessor` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（23/20 个样本）：Steps较低可能导致细节不足
