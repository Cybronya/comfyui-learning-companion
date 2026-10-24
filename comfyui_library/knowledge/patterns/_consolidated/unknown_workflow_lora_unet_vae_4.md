---
name: unknown_workflow_lora_unet_vae_4
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.863667
common_nodes: [CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1 一键透视光影融图｜产品完美融入背景_2109059569963069441.json, 图片生成/图生图/Qwen Image 2.1 一键透视光影融图｜产品完美融入背景_2109192704059072513.json, 图片生成/图生图/Qwen Image 2.1 一键透视光影融图｜产品完美融入背景_2110678471289696258.json, 图片生成/图生图/Qwen image 2.1 一键模特换装｜服装迁移_2111691946950483969.json, 图片生成/图生图/Qwen image 2.1 人物姿势图转白模_2107830881904848898.json, 图片生成/图生图/Qwen image 2.1 动漫人物转真人_2107971466020081665.json, 图片生成/图生图/Qwen-image2.1-图像角色多角度lora_2111388449549930497.json, 图片生成/图生图/Qwen-image2.1-图像高清修复_2111633650839285761.json, 图片生成/图生图/Qwen-image2.1-服装迁移_2111640579607195649.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_4

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 一键透视光影融图｜产品完美融入背景_2109059569963069441.json、图片生成/图生图/Qwen Image 2.1 一键透视光影融图｜产品完美融入背景_2109192704059072513.json、图片生成/图生图/Qwen Image 2.1 一键透视光影融图｜产品完美融入背景_2110678471289696258.json、图片生成/图生图/Qwen image 2.1 一键模特换装｜服装迁移_2111691946950483969.json、图片生成/图生图/Qwen image 2.1 人物姿势图转白模_2107830881904848898.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/9 个有
- `KSampler` —— 6/9 个有
- `VAEDecode` —— 6/9 个有
- `孤海注释` —— 6/9 个有
- `ImpactInt` —— 5/9 个有
- `Int` —— 4/9 个有
- `KSampler (Efficient)` —— 3/9 个有
- `easy seed` —— 3/9 个有
- `PreviewImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 30 | 9 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，9 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
