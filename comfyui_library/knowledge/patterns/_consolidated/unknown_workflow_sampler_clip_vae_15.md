---
name: unknown_workflow_sampler_clip_vae_15
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.941091
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/极速版文生图V1-Qwen-ImageNunchaku Ran_2046513028291633154.json, 图片生成/文生图/炼狱杏寿郎_1981285976733638658.json, 图片生成/文生图/猩红共生体变身与感染_2051256128578830338.json, 图片生成/文生图/瓷影墨韵：新中式IP手办设计_2056251017632768001.json, 图片生成/文生图/电商生成多镜头图片 qwen2512_2017062093035413506.json, 图片生成/文生图/红潮造相ZImage+LoRA文生图+VAE增加细节_2009818930566664194.json, 图片生成/文生图/赛博玄幻修仙者｜墨渊·文生图_2093285763407507458.json, 图片生成/文生图/赛博玄幻修仙者｜燕青·文生图_2093374844577599489.json, 图片生成/文生图/超可爱的q版3d风格动画角色设计_2067581459497578498.json, 图片生成/文生图/（贞贞版4图版）Qwen 2512 Kook千问美人+真实幻想+极致真实文生图V1_2008746844083462145.json, 图片生成/文生图/（贞贞版）Z-Image-Base 2w2步_2016755186840113154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_15

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/极速版文生图V1-Qwen-ImageNunchaku Ran_2046513028291633154.json、图片生成/文生图/炼狱杏寿郎_1981285976733638658.json、图片生成/文生图/猩红共生体变身与感染_2051256128578830338.json、图片生成/文生图/瓷影墨韵：新中式IP手办设计_2056251017632768001.json、图片生成/文生图/电商生成多镜头图片 qwen2512_2017062093035413506.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/11 个有
- `UNETLoader` —— 10/11 个有
- `ModelSamplingAuraFlow` —— 9/11 个有
- `CR Prompt Text` —— 2/11 个有
- `LayerUtility: PurgeVRAM` —— 2/11 个有
- `CR Text` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `LatentUpscaleBy` —— 1/11 个有
- `NunchakuQwenImageDiTLoader` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 11 | 12% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 37% |
| 采样算法 | euler | - | 11 | 73% |
| 调度器 | simple | - | 11 | 45% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，11 个样本，取值分散，一致性仅 12%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 37%
- 采样算法 最常用 euler，11 个样本，一致性 73%
- 调度器 最常用 simple，11 个样本，一致性 45%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（7/11 个样本）：Steps较低可能导致细节不足
