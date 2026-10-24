---
name: unknown_workflow_sampler_unet_vae_6
type: Unknown Workflow
frequency: 24
level: strong
coverage: 0.838375
common_nodes: [CLIPLoader, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen Image 2.1 PE 文生图_2102401855983808514.json, 图片生成/图生图/BF16小字不崩-Qwen image 2.1图片编辑_2102282925260759042.json, 图片生成/图生图/BF16小字不崩-Qwen_image_2.1图片编辑_2104378058986844161.json, 图片生成/图生图/BFS换脸6步加速版Qwen_Image_2.1图像编辑_2108752507940986881.json, 图片生成/图生图/BFS换脸6步加速版Qwen_Image_2.1图像编辑_2110554314409332737.json, 图片生成/图生图/Qwen 2.1 图像编辑（4步加速）_2102704302576988161.json, 图片生成/图生图/Qwen Image 2.1 PE 图像编辑-t8加速版_2105710865591922690.json, 图片生成/图生图/Qwen Image 2.1 PE 图像编辑2609_2106042591421747201.json, 图片生成/图生图/Qwen Image 2.1 参考人物姿势_2102935036923310081.json, 图片生成/图生图/Qwen Image 2.1 整张图像编辑_2102952588135194626.json, 图片生成/图生图/（BFS换脸6步加速版）Qwen Image 2.1图像编辑_2103909503581380610.json, 图片生成/图生图/（稳定加速版）Qwen Image 2.1 PE 图像编辑_2102954366490734594.json, 图片生成/图生图/（稳定加速版）Qwen Image 2.1 PE 姿势编辑_2103743196265275394.json, 图片生成/图生图/（贞贞lora-图像编辑）Qwen Image 2.1 PE 姿势编辑_2105844300620853250.json, 图片生成/文生图/Qwen Image 2.1 PE 文生图2609_2106042102424629249.json, 图片生成/文生图/Qwen Image 2.1 PE 文生图_2102653627042189314.json, 图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（优化版）_2103650787716059138.json, 图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（图生图编辑版）_2103658795657424897.json, 图片生成/文生图/（稳定加速版）Qwen Image 2.1 PE 文生图_2102956400250023938.json, 数字人/数字人/（稳定加速版）Qwen Image 2.1 PE 图像编辑_2103878968540745729.json, 视频生成/图生视频/Qwen_Image_2.1_PE_图像编辑_2104045367338823681.json, 视频生成/图生视频/Qwen_Image_2.1_参考人物姿势_2102963142430126082.json, 视频生成/文生视频/Qwen_Image_2.1_PE_文生图_2104447077903323137.json, 视频生成/文生视频/Qwen_Image_2.1_文生图-PE版_2106926003867185154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_6

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1 PE 文生图_2102401855983808514.json、图片生成/图生图/BF16小字不崩-Qwen image 2.1图片编辑_2102282925260759042.json、图片生成/图生图/BF16小字不崩-Qwen_image_2.1图片编辑_2104378058986844161.json、图片生成/图生图/BFS换脸6步加速版Qwen_Image_2.1图像编辑_2108752507940986881.json、图片生成/图生图/BFS换脸6步加速版Qwen_Image_2.1图像编辑_2110554314409332737.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 22/24 个有
- `QwenPERewriteT8` —— 22/24 个有
- `easy cleanGpuUsed` —— 22/24 个有
- `easy showAnything` —— 22/24 个有
- `LoadImage` —— 17/24 个有
- `QwenImage21SageAttentionT8` —— 16/24 个有
- `QwenImage21BlockCacheT8` —— 13/24 个有
- `QwenImage21SpectrumT8` —— 13/24 个有
- `EmptyImage` —— 5/24 个有
- `LoraLoaderModelOnly` —— 5/24 个有
- `PreviewImage` —— 5/24 个有
- `ConcatTextOfUtils` —— 4/24 个有
- `LoraLoaderBypassModelOnly` —— 3/24 个有
- `AIO_Preprocessor` —— 2/24 个有
- `SaveImageAdvanced` —— 2/24 个有
- `Lora Loader Stack (rgthree)` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 4 - 50 | 24 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 24 | 100% |
| 采样算法 | euler | - | 24 | 100% |
| 调度器 | simple | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 24 | 100% |
| 高度 | 1024 | 1024 - 1024 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 4 - 50，24 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，24 个样本，一致性 100%
- 调度器 最常用 simple，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，24 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，24 个样本，取值集中（一致性 100%）
