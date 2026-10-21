---
name: unknown_workflow_sampler_clip_unet_68
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.929111
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/PBR材质生成 模型贴图生成 z-image+育碧开源CHORD模型_1998964415804399617.json, 图片生成/文生图/QwenImage 8步 蒸馏加速工作流_2084844216345251842.json, 图片生成/文生图/QwenImage 8步 蒸馏加速工作流_2084906463855726594.json, 图片生成/文生图/QwenImage 8步 蒸馏加速工作流_2087826566675001345.json, 图片生成/文生图/QwenImage+8步+蒸馏加速工作流_2015669597445300226.json, 图片生成/文生图/Y-Z-Image-turbo+lenovo lora-workflow_1995640202892861441.json, 图片生成/文生图/【老金驿站】4步Qwen2512极速lighiting出图工作流_2006643426929938433.json, 图片生成/文生图/材质贴图生成_2018526649268051969.json, 图片生成/文生图/🎮育碧开源CHORD大模型，一句话生成3A游戏级PBR贴图！_2004035810066350082.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_68

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/PBR材质生成 模型贴图生成 z-image+育碧开源CHORD模型_1998964415804399617.json、图片生成/文生图/QwenImage 8步 蒸馏加速工作流_2084844216345251842.json、图片生成/文生图/QwenImage 8步 蒸馏加速工作流_2084906463855726594.json、图片生成/文生图/QwenImage 8步 蒸馏加速工作流_2087826566675001345.json、图片生成/文生图/QwenImage+8步+蒸馏加速工作流_2015669597445300226.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 8/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `ChordLoadModel` —— 3/9 个有
- `ChordMaterialEstimation` —— 3/9 个有
- `ChordNormalToHeight` —— 3/9 个有
- `ResizeAndPadImage` —— 3/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `CFGNorm` —— 1/9 个有
- `SDXLAspectRatio` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 9 | 9 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 9，9 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
