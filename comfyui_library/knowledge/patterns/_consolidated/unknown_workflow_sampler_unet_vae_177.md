---
name: unknown_workflow_sampler_unet_vae_177
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.903333
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenPERewriteT8, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-image-2.1_姿势参考编辑_2103050481391194113.json, 图片生成/图生图/Qwen_Image_2.1-图像编辑_2103057203816132609.json, 图片生成/图生图/Qwen_Image_2.1-透明图像编辑_2103060343198142466.json, 图片生成/图生图/Qwen_Image_2.1_PE提示词优化_提取服装_3D展示_精修褶皱_2105584897179086849.json, 图片生成/图生图/Qwen_Image_2.1_PE提示词优化_提取服装_3D展示_精修褶皱_2108370520688390145.json, 图片生成/文生图/Qwen Image 2.1 PE提示词优化 提取服装 3D展示 精修褶皱_2103745672011935746.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_177

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-image-2.1_姿势参考编辑_2103050481391194113.json、图片生成/图生图/Qwen_Image_2.1-图像编辑_2103057203816132609.json、图片生成/图生图/Qwen_Image_2.1-透明图像编辑_2103060343198142466.json、图片生成/图生图/Qwen_Image_2.1_PE提示词优化_提取服装_3D展示_精修褶皱_2105584897179086849.json、图片生成/图生图/Qwen_Image_2.1_PE提示词优化_提取服装_3D展示_精修褶皱_2108370520688390145.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenPERewriteT8`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImage21BlockCacheT8` —— 4/6 个有
- `QwenImage21SageAttentionT8` —— 4/6 个有
- `QwenImage21SpectrumT8` —— 4/6 个有
- `ComfySwitchNode` —— 3/6 个有
- `Display Any (rgthree)` —— 3/6 个有
- `ImageStitch` —— 3/6 个有
- `JjkText` —— 3/6 个有
- `Text Multiline` —— 3/6 个有
- `easy seed` —— 3/6 个有
- `QwenImage21Cache` —— 2/6 个有
- `GetNode` —— 1/6 个有
- `SetNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 40 - 50 | 6 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 40 - 50，6 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
