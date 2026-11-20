---
name: unknown_workflow_sampler_clip_unet_72
type: Unknown Workflow
frequency: 14
level: weak
coverage: 0.9465
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-turbo-fp8 基础文生图_1994352646947475457.json, 图片生成/文生图/Z-image-turbo-t2i_2073765816608313345.json, 图片生成/文生图/Z-image-文生图工作流_2103815728557281281.json, 图片生成/文生图/Z-image-淡妆浓抹V3.0文生图_2026649178574688257.json, 图片生成/文生图/Z-image-超现实模型3.0_2021938613541412866.json, 图片生成/文生图/Z-image基础文生图_2017017701364932609.json, 图片生成/文生图/Z-image文生图-像素艺术风格_1999249293112377346.json, 图片生成/文生图/Z-image文生图8步Lora2602_2028594976501800961.json, 图片生成/文生图/Z-image文生图GGUF.json_2057397174631223298.json, 图片生成/文生图/comfyui教学第一期-文生图_2008024786936537089.json, 图片生成/文生图/qwen-image文生图4step加速_2033447038481866754.json, 图片生成/文生图/z-image Engineer 打光lora 真实lora测试_2033372581125955586.json, 图片生成/文生图/z_image_turbo文生图_2011271534962286593.json, 图片生成/文生图/z_image_文生图（儿童）_2034571865527685121.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_72

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Z-image-turbo-fp8 基础文生图_1994352646947475457.json、图片生成/文生图/Z-image-turbo-t2i_2073765816608313345.json、图片生成/文生图/Z-image-文生图工作流_2103815728557281281.json、图片生成/文生图/Z-image-淡妆浓抹V3.0文生图_2026649178574688257.json、图片生成/文生图/Z-image-超现实模型3.0_2021938613541412866.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 13/14 个有
- `VAELoader` —— 13/14 个有
- `ConditioningZeroOut` —— 11/14 个有
- `LoraLoaderModelOnly` —— 10/14 个有
- `CLIPLoaderGGUF` —— 2/14 个有
- `LayerUtility: PurgeVRAM V2` —— 2/14 个有
- `PrimitiveStringMultiline` —— 2/14 个有
- `AV_VAELoader` —— 1/14 个有
- `PrimitiveString` —— 1/14 个有
- `ResolutionSelector` —— 1/14 个有
- `easy promptConcat` —— 1/14 个有
- `easy showAnything` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 4 - 50 | 14 | 9% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 14 | 65% |
| 采样算法 | res_multistep | - | 14 | 50% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 1 | 0.9 - 1 | 14 | 97% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 4 - 50，14 个样本，取值分散，一致性仅 9%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，14 个样本
- 采样算法 最常用 res_multistep，14 个样本，一致性 50%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，14 个样本，取值集中（一致性 97%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
