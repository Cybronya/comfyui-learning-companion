---
name: unknown_workflow_sampler_unet_vae_125
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.83675
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed-Image快速证件照_2046791496526995458.json, 图片生成/图生图/Qwen Edit Plus 人物换背景_1971655794066452481.json, 图片生成/图生图/Qwen Edit Plus 去除图片水印_1968538239810318338.json, 图片生成/图生图/QwenEdit Plus 修改文字_1968557266519633922.json, 图片生成/图生图/QwenEdit Plus 生成手办_1970471630713593857.json, 图片生成/图生图/国庆头像 Qwen Edit 无位移风格转绘_1969928665675034625.json, 图片生成/图生图/国庆头像_Qwen_Edit_无位移背景切换_1969973272295206913.json, 图片生成/图生图/小志 QwenEdit 解决偏移问题_1968284089998553089.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_125

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FireRed-Image快速证件照_2046791496526995458.json、图片生成/图生图/Qwen Edit Plus 人物换背景_1971655794066452481.json、图片生成/图生图/Qwen Edit Plus 去除图片水印_1968538239810318338.json、图片生成/图生图/QwenEdit Plus 修改文字_1968557266519633922.json、图片生成/图生图/QwenEdit Plus 生成手办_1970471630713593857.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 7/8 个有
- `Image Comparer (rgthree)` —— 6/8 个有
- `JjkText` —— 6/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 4/8 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 4/8 个有
- `RH_Translator` —— 2/8 个有
- `EmptyLatentImage` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `TextCombinerSix` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1016 | - | 1 | 100% |
| 高度 | 1536 | - | 1 | 100% |
| 采样步数 | 22.5 | 8 - 30 | 8 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 8 | 40% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | beta57 | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 22.5，观测区间 8 - 30，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 beta57，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
