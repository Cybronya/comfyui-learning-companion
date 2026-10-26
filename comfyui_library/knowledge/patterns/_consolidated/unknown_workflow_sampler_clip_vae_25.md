---
name: unknown_workflow_sampler_clip_vae_25
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.89125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/极速版文生图V1-Qwen-ImageNunchaku Ran_2046513028291633154.json, 图片生成/文生图/海报生成器+QwenImage=艾橘溪_1954567812612288513.json, 图片生成/文生图/炼狱杏寿郎_1981285976733638658.json, 图片生成/文生图/猩红共生体变身与感染_2051256128578830338.json, 图片生成/文生图/电商生成多镜头图片 qwen2512_2017062093035413506.json, 图片生成/文生图/艺术字体生成器+QwenImage=B站艾橘溪_1954565922696654850.json, 图片生成/文生图/（贞贞版3W步绝美版）Z-Image-Base文生图V1_2016831860403343362.json, 图片生成/文生图/（贞贞版）Z-Image-Base 2w2步_2016755186840113154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_25

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/极速版文生图V1-Qwen-ImageNunchaku Ran_2046513028291633154.json、图片生成/文生图/海报生成器+QwenImage=艾橘溪_1954567812612288513.json、图片生成/文生图/炼狱杏寿郎_1981285976733638658.json、图片生成/文生图/猩红共生体变身与感染_2051256128578830338.json、图片生成/文生图/电商生成多镜头图片 qwen2512_2017062093035413506.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `LayerUtility: PurgeVRAM` —— 3/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `NunchakuQwenImageDiTLoader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | 8 - 50 | 8 | 33% |
| Prompt 约束强度(CFG) | 3.25 | 1 - 5 | 8 | 47% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 22.5，观测区间 8 - 50，8 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 3.25，观测区间 1 - 5，8 个样本，取值分散，一致性仅 47%
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
