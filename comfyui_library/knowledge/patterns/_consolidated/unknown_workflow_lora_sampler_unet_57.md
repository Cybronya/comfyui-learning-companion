---
name: unknown_workflow_lora_sampler_unet_57
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9368
common_nodes: [CLIPLoader, ConditioningZeroOut, ImageStitch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Nunchaku-Pose姿势参考-千问Edit2509图像编辑_1971205875295830018.json, 图片生成/图生图/Nunchaku-人物首尾帧制作-Edit2509图像编辑_1971207824632168449.json, 图片生成/图生图/Nunchaku-人物首尾帧制作-Edit2509图像编辑_1971210529568149505.json, 图片生成/图生图/Nunchaku-证件照-Edit2509图像编辑_1971199922907336705.json, 图片生成/图生图/Pose姿势参考-千问Edit2509图像编辑_1970828887754186753.json, 图片生成/图生图/Pose姿势参考-千问Edit2509图像编辑_1971040326016212994.json, 图片生成/图生图/Qwen-Image-Edit_2509单图融合编辑【Nunchaku版】_1971933422384050178.json, 图片生成/图生图/qwen-2511 Cosplay任何角色_2028679612187811842.json, 图片生成/图生图/千问Edit2509图像编辑-多图结婚照_1971036029203423233.json, 图片生成/图生图/多人场景融合-千问Edit2509图像编辑_1970822561934282754.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_57

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Nunchaku-Pose姿势参考-千问Edit2509图像编辑_1971205875295830018.json、图片生成/图生图/Nunchaku-人物首尾帧制作-Edit2509图像编辑_1971207824632168449.json、图片生成/图生图/Nunchaku-人物首尾帧制作-Edit2509图像编辑_1971210529568149505.json、图片生成/图生图/Nunchaku-证件照-Edit2509图像编辑_1971199922907336705.json、图片生成/图生图/Pose姿势参考-千问Edit2509图像编辑_1970828887754186753.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `ImageStitch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 9/10 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 9/10 个有
- `NunchakuQwenImageDiTLoader` —— 5/10 个有
- `AIO_Preprocessor` —— 3/10 个有
- `PrimitiveInt` —— 3/10 个有
- `Image Comparer (rgthree)` —— 2/10 个有
- `ImageConcanate` —— 2/10 个有
- `ImageConcatMulti` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `Seed (rgthree)` —— 2/10 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/10 个有
- `Anything Everywhere3` —— 1/10 个有
- `RH_LLMAPI_NODE` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 10 | 67% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 10 | 73% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | beta57 | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 beta57，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
