---
name: image_to_image_lora_sampler_unet_33
type: Image To Image
frequency: 14
level: strong
coverage: 0.972
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/局部修改 qwen2511_2099530960969756674.json, 图片生成/图生图/常用_图片_qwen2511单图_2037736525001138178.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096660074356887553.json, 图片生成/图生图/真人转动漫  真人转卡通 真人转漫画   真人转3D Q版卡通_2053901548941529090.json, 图片生成/图生图/真人转卡通  真人转漫画 真人转动漫  Q版卡通  Q版风格化_2053721157651714049.json, 图片生成/图生图/真人转卡通  真人转漫画 真人转动漫  Q版卡通  Q版风格化_2053845599967031297.json, 图片生成/图生图/真人转卡通  真人转漫画 真人转动漫  Q版卡通  Q版风格化_2053867268517449729.json, 图片生成/图生图/真人转卡通  真人转漫画 真人转动漫  Q版卡通  Q版风格化_2053869198199279618.json, 图片生成/图生图/真人转卡通 真人转漫画 真人转动漫  真人转3D Q版卡通_2053848663335677953.json, 图片生成/图生图/真人转卡通 真人转漫画 真人转动漫  真人转3D Q版卡通_2053871652357844993.json, 图片生成/图生图/真人转卡通 真人转漫画 真人转动漫  真人转3D Q版卡通_2053877533954854913.json, 图片生成/图生图/老金驿站】Qwen单图溶图4步极速工作流_1958797125020774402.json, 图片生成/图生图/（单图推荐）tele style画风迁移，游戏_动漫角色设计_2054939690477858817.json, 图片生成/图生图/👾怪獸-千问多图编辑8步版👾_1977240342351237121.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_33

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/局部修改 qwen2511_2099530960969756674.json、图片生成/图生图/常用_图片_qwen2511单图_2037736525001138178.json、图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096660074356887553.json、图片生成/图生图/真人转动漫  真人转卡通 真人转漫画   真人转3D Q版卡通_2053901548941529090.json、图片生成/图生图/真人转卡通  真人转漫画 真人转动漫  Q版卡通  Q版风格化_2053721157651714049.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEdit` —— 10/14 个有
- `PathchSageAttentionKJ` —— 4/14 个有
- `TextEncodeQwenImageEditPlus` —— 4/14 个有
- `ImageScaleToTotalPixels` —— 3/14 个有
- `ImageConcatMulti` —— 2/14 个有
- `PrimitiveStringMultiline` —— 2/14 个有
- `ConditioningZeroOut` —— 1/14 个有
- `DWPreprocessor` —— 1/14 个有
- `EmptyImage` —— 1/14 个有
- `ModelPatchTorchSettings` —— 1/14 个有
- `ResizeLongestToNode` —— 1/14 个有
- `easy cleanGpuUsed` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 14 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
