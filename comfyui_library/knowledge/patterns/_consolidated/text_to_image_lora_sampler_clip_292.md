---
name: text_to_image_lora_sampler_clip_292
type: Text To Image
frequency: 7
level: moderate
coverage: 0.947571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN 图像旋转万能视角调整_2015957553431187458.json, 图片生成/图生图/Qwen image 人物一致性 多图展示_2044669602428362753.json, 图片生成/图生图/fireRed_edit_workflow_2025984865023299586.json, 图片生成/图生图/fireRed_edit_workflow_2029377409757224961.json, 图片生成/图生图/multiple2511 图片多角度、多视角编辑工作流_2013173343419109378.json, 图片生成/图生图/qwen_multiple2511 图片多角度、多视角编辑工作流_2046132302052331522.json, 图片生成/图生图/seedance2.0真人过审-Sim制作_2053052803047804930.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_292

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/QWEN 图像旋转万能视角调整_2015957553431187458.json、图片生成/图生图/Qwen image 人物一致性 多图展示_2044669602428362753.json、图片生成/图生图/fireRed_edit_workflow_2025984865023299586.json、图片生成/图生图/fireRed_edit_workflow_2029377409757224961.json、图片生成/图生图/multiple2511 图片多角度、多视角编辑工作流_2013173343419109378.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 6/7 个有
- `GetImageSize` —— 4/7 个有
- `QwenMultiangleCameraNode` —— 4/7 个有
- `ImageScaleToTotalPixels` —— 3/7 个有
- `JjkText` —— 2/7 个有
- `easy imageSize` —— 2/7 个有
- `ConditioningConcat` —— 1/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `ImageResize+` —— 1/7 个有
- `SeedVR2` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 7 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 856 | 720 - 1280 | 7 | 73% |
| 高度 | 720 | 480 - 1280 | 7 | 66% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，7 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 856，观测区间 720 - 1280，7 个样本
- 高度 中位数 720，观测区间 480 - 1280，7 个样本
- 高发问题（18/7 个样本）：Steps较低可能导致细节不足
