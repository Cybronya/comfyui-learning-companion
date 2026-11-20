---
name: unknown_workflow_lora_sampler_unet_74
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.976222
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/03 hyfimage_2048365509980200962.json, 图片生成/反推提示词/36addtexttoimage_2049771863429140482.json, 图片生成/反推提示词/3jqggfppxlb_2059682402812911617.json, 图片生成/反推提示词/48dantubianji_2050122316616617985.json, 图片生成/图生图/五图编辑-rh-Qwen-Edit-2511-模板_2014144550574493697.json, 图片生成/图生图/单图编辑-rh-Qwen-Edit-2511-模板_2013616947384029186.json, 图片生成/图生图/叁图编辑-rh-Qwen-Edit-2511-模板_2013999350959054850.json, 图片生成/图生图/双图编辑-Qwen-Edit-2511-模板_2013899588947681282.json, 图片生成/图生图/四图编辑-rh-Qwen-Edit-2511-模板_2014144556878536705.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_74

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/03 hyfimage_2048365509980200962.json、图片生成/反推提示词/36addtexttoimage_2049771863429140482.json、图片生成/反推提示词/3jqggfppxlb_2059682402812911617.json、图片生成/反推提示词/48dantubianji_2050122316616617985.json、图片生成/图生图/五图编辑-rh-Qwen-Edit-2511-模板_2014144550574493697.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/9 个有
- `EmptySD3LatentImage` —— 6/9 个有
- `RTXVideoSuperResolution` —— 4/9 个有
- `SmartImageConcat` —— 4/9 个有
- `LoadLynxResampler` —— 2/9 个有
- `LynxEncodeFaceIP` —— 2/9 个有
- `LynxInsightFaceCrop` —— 2/9 个有
- `JjkText` —— 1/9 个有
- `ShellAgentPluginOutputText` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 9 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | sa_solver | - | 9 | 67% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，9 个样本，一致性 67%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
