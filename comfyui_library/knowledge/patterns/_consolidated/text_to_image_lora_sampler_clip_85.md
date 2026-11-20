---
name: text_to_image_lora_sampler_clip_85
type: Text To Image
frequency: 14
level: strong
coverage: 0.888429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2.1五视图透明背景，图生图多视角角色设计工具_2103985760100765697.json, 图片生成/图生图/Qwen 2.1动漫转写实工作流，无需触发词图生图动漫风格写实化处理_2105769532047577090.json, 图片生成/图生图/Qwen 2.1图片编辑工作流，简洁高效的图生图处理方案_2103906470701129730.json, 图片生成/图生图/Qwen 2.1改头换面换头术 人物面部精准替换_2104991945562087425.json, 图片生成/图生图/Qwen 2.1改头换面换头术｜图生图精准换脸｜换头不换身效果自然_2104761533778718721.json, 图片生成/图生图/Qwen Image 2.1 Turbo人物角色替换 人物一致性更强_2109408658609238018.json, 图片生成/图生图/Qwen Image 2.1 Turbo人物角色替换 人物一致性更强_2109748589525295106.json, 图片生成/图生图/Qwen Image 2.1 Turbo多图像编辑8步快速出图 高效改图方案_2109334660395393026.json, 图片生成/图生图/Qwen Image 2.1 Turbo多图像编辑8步快速出图 高效改图方案_2109696542016884738.json, 图片生成/图生图/Qwen image 2.1人物换脸｜写真级换脸效果自然不穿帮_2111106231317389313.json, 图片生成/图生图/Qwen image 2.1智能换装，图生图服装替换自然贴合_2110528939180515330.json, 图片生成/图生图/Qwen_image_2.1智能换装，图生图服装替换自然贴合_2111273115165749250.json, 图片生成/图生图/Qwen_image_2.1智能换装，图生图服装替换自然贴合_2114261870923304961.json, 图片生成/图生图/Qwen_image_2.1智能换装，服装替换自然贴合图生图_2111952478379003906.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_85

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen 2.1五视图透明背景，图生图多视角角色设计工具_2103985760100765697.json、图片生成/图生图/Qwen 2.1动漫转写实工作流，无需触发词图生图动漫风格写实化处理_2105769532047577090.json、图片生成/图生图/Qwen 2.1图片编辑工作流，简洁高效的图生图处理方案_2103906470701129730.json、图片生成/图生图/Qwen 2.1改头换面换头术 人物面部精准替换_2104991945562087425.json、图片生成/图生图/Qwen 2.1改头换面换头术｜图生图精准换脸｜换头不换身效果自然_2104761533778718721.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 12/14 个有
- `ResolutionSelector` —— 11/14 个有
- `Image Comparer (rgthree)` —— 10/14 个有
- `ComfySwitchNode` —— 9/14 个有
- `CR Text` —— 7/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/14 个有
- `ImageConcanate` —— 5/14 个有
- `Latent Switch (JPS)` —— 5/14 个有
- `EmptyImage` —— 3/14 个有
- `PreviewImage` —— 3/14 个有
- `QwenImagePromptOptimizer` —— 2/14 个有
- `easy imageSave` —— 2/14 个有
- `easy showAnything` —— 2/14 个有
- `CR Prompt List` —— 1/14 个有
- `HAIGC_SaveImagesToZip` —— 1/14 个有
- `MultiTextConcatenate` —— 1/14 个有
- `PlaySound|pysssss` —— 1/14 个有
- `PrimitiveInt` —— 1/14 个有
- `PrimitiveStringMultiline` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（24/14 个样本）：Steps较低可能导致细节不足
