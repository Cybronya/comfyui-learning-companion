---
name: unknown_workflow_sampler_clip_unet_185
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.929143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/星绘-Z-image-base-Z-Image-tuber对比整合_2016355882694615042.json, 图片生成/文生图/2031214053871329282.json, 图片生成/文生图/HeGenAI-N8N-QWEN-基础文生图_1968571302049140738.json, 图片生成/文生图/Nunchaku Qwen-Image和官版8步对比_1964982995616677890.json, 图片生成/文生图/Qwen-Image 8步和4步对比_1955342392250417153.json, 图片生成/文生图/Qwen-Image-lightning+LoRA+多步骤对比_1955290519761928194.json, 图片生成/文生图/qwen-image加速生图4步8步20步对比工作流_1954915934088544258.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_185

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/星绘-Z-image-base-Z-Image-tuber对比整合_2016355882694615042.json、图片生成/文生图/2031214053871329282.json、图片生成/文生图/HeGenAI-N8N-QWEN-基础文生图_1968571302049140738.json、图片生成/文生图/Nunchaku Qwen-Image和官版8步对比_1964982995616677890.json、图片生成/文生图/Qwen-Image 8步和4步对比_1955342392250417153.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `LayerUtility: ImageReel` —— 5/7 个有
- `LayerUtility: ImageReelComposit` —— 5/7 个有
- `PreviewImage` —— 4/7 个有
- `CR Text` —— 2/7 个有
- `INTConstant` —— 2/7 个有
- `CR SDXL Aspect Ratio` —— 1/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `DF_Get_image_size` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `NunchakuQwenImageDiTLoader` —— 1/7 个有
- `StringConcatenate` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 7 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 32% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，7 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（11/7 个样本）：Steps较低可能导致细节不足
