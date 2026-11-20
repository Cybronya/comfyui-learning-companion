---
name: unknown_workflow_sampler_unet_vae_16
type: Unknown Workflow
frequency: 21
level: strong
coverage: 0.83619
common_nodes: [CLIPLoader, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, KSampler, QwenPERewriteT8, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/提示词自动优化Qwen Image 2.1 PE 多图像编辑-t8的pe高质量版_2102243596664655874.json, 图片生成/图生图/稳定加速版Qwen_Image_2.1_PE_姿势编辑_2108764188251348994.json, 图片生成/图生图/稳定加速版Qwen_Image_2.1_PE_姿势编辑_2110555697225232386.json, 图片生成/图生图/超级加速版Qwen Image 2.1 PE 图像编辑_2103518802859352065.json, 图片生成/图生图/（4步加速-v0.21适配版）Qwen Image 2.1 PE 图像编辑（最多3图）_2103127729746042881.json, 图片生成/图生图/（4步加速-非稳定）Qwen Image 2.1 PE 图像编辑（最多3图）_2102757842590724097.json, 图片生成/图生图/（BFS换脸6步加速版）Qwen Image 2.1图像编辑_2103909503581380610.json, 图片生成/图生图/（Pruna-5步加速-非稳定）Qwen Image 2.1 PE 图像编辑_2103704266870448129.json, 图片生成/图生图/（Pruna-8步加速-非稳定）Qwen Image 2.1 PE 图像编辑（最多3图）_2103706738779320321.json, 图片生成/图生图/（Remove模型测试）Qwen Image 2.1 PE 姿势编辑_2106228938317062146.json, 图片生成/图生图/（Remove模型）Qwen Image 2.1 PE 姿势编辑_2106290030498111489.json, 图片生成/图生图/（Remove模型）Qwen Image 2.1 PE 姿势编辑_2106383894743441409.json, 图片生成/图生图/（稳定加速版）Qwen Image 2.1 PE 图像编辑_2102954366490734594.json, 图片生成/图生图/（稳定加速版）Qwen Image 2.1 PE 姿势编辑_2103743196265275394.json, 图片生成/图生图/（贞贞lora-图像编辑）Qwen Image 2.1 PE 姿势编辑_2105844300620853250.json, 图片生成/文生图/Qwen Image 2.1 PE 文生图2609_2106042102424629249.json, 图片生成/文生图/Qwen Image 2.1 PE 文生图_2102653627042189314.json, 图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（优化版）_2103650787716059138.json, 图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（图生图编辑版）_2103658795657424897.json, 图片生成/文生图/（稳定加速版）Qwen Image 2.1 PE 文生图_2102956400250023938.json, 数字人/数字人/（稳定加速版）Qwen Image 2.1 PE 图像编辑_2103878968540745729.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_16

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/提示词自动优化Qwen Image 2.1 PE 多图像编辑-t8的pe高质量版_2102243596664655874.json、图片生成/图生图/稳定加速版Qwen_Image_2.1_PE_姿势编辑_2108764188251348994.json、图片生成/图生图/稳定加速版Qwen_Image_2.1_PE_姿势编辑_2110555697225232386.json、图片生成/图生图/超级加速版Qwen Image 2.1 PE 图像编辑_2103518802859352065.json、图片生成/图生图/（4步加速-v0.21适配版）Qwen Image 2.1 PE 图像编辑（最多3图）_2103127729746042881.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `QwenPERewriteT8`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 19/21 个有
- `LoadImage` —— 17/21 个有
- `QwenImage21SageAttentionT8` —— 16/21 个有
- `QwenImage21BlockCacheT8` —— 15/21 个有
- `QwenImage21SpectrumT8` —— 15/21 个有
- `LoraLoaderModelOnly` —— 8/21 个有
- `PathchSageAttentionKJ` —— 4/21 个有
- `ConcatTextOfUtils` —— 2/21 个有
- `LoraLoaderBypassModelOnly` —— 2/21 个有
- `Lora Loader Stack (rgthree)` —— 1/21 个有
- `PrimitiveBoolean` —— 1/21 个有
- `孤海注释` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 4 - 40 | 21 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 21 | 100% |
| 采样算法 | euler | - | 21 | 100% |
| 调度器 | simple | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 21 | 100% |
| 高度 | 1024 | 1024 - 1024 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 4 - 40，21 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，21 个样本，一致性 100%
- 调度器 最常用 simple，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，21 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，21 个样本，取值集中（一致性 100%）
