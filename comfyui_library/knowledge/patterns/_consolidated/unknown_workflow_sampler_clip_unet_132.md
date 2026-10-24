---
name: unknown_workflow_sampler_clip_unet_132
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.876889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen 文生图(二次元)_2057795247358435330.json, 图片生成/文生图/Qwen 文生图_1955160402595233794.json, 图片生成/文生图/Qwen 文生图工作流--@橘子_SJRJT_1962804112075173889.json, 图片生成/文生图/Qwen-Image 2steps 超极速生图_2028108869695709185.json, 图片生成/文生图/Qwen-Image ComfyUI原生工作流_1970739735536824321.json, 图片生成/文生图/Qwen-Image ComfyUI原生工作流_2027264283821744129.json, 图片生成/文生图/Qwen-Image-2512-Wuli_2007448165187854338.json, 图片生成/文生图/Qwen-Image-2512-lightx2v_2007448158065922050.json, 图片生成/文生图/Qwen-Image-8步和4步对比_1955503632722661377.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_132

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Qwen 文生图(二次元)_2057795247358435330.json、图片生成/文生图/Qwen 文生图_1955160402595233794.json、图片生成/文生图/Qwen 文生图工作流--@橘子_SJRJT_1962804112075173889.json、图片生成/文生图/Qwen-Image 2steps 超极速生图_2028108869695709185.json、图片生成/文生图/Qwen-Image ComfyUI原生工作流_1970739735536824321.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：88%

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
- `LoraLoaderModelOnly` —— 8/9 个有
- `easy seed` —— 3/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `AddLabel` —— 1/9 个有
- `CFGNorm` —— 1/9 个有
- `ImageConcanate` —— 1/9 个有
- `LayerUtility: TextJoin` —— 1/9 个有
- `String Literal` —— 1/9 个有
- `Text` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 2 - 12 | 9 | 46% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 9 | 53% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 2 - 12，9 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（30/9 个样本）：Steps较低可能导致细节不足
