---
name: image_to_image_lora_sampler_unet_144
type: Image To Image
frequency: 5
level: strong
coverage: 0.8966
common_nodes: [CLIPLoader, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/🥯Qwen-next scene人物一致自动分镜控制🥯_1983051929599246337.json, 图片生成/文生图/qwen2509文生图短剧分镜图片_2010143977151930370.json, 图片生成/文生图/全能版-根据主题自动分镜剧本图_1986359513102118913.json, 图片生成/文生图/视频生成-生成分镜图片_2012090015605596162.json, 图片生成/文生图/视频生成-生成分镜图片多角色_2098296059050160129.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_144

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/🥯Qwen-next scene人物一致自动分镜控制🥯_1983051929599246337.json、图片生成/文生图/qwen2509文生图短剧分镜图片_2010143977151930370.json、图片生成/文生图/全能版-根据主题自动分镜剧本图_1986359513102118913.json、图片生成/文生图/视频生成-生成分镜图片_2012090015605596162.json、图片生成/文生图/视频生成-生成分镜图片多角色_2098296059050160129.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `ImpactInt` —— 2/5 个有
- `JoinStringMulti` —— 2/5 个有
- `ProcessString` —— 2/5 个有
- `RH_LLMAPI_NODE` —— 2/5 个有
- `easy convertAnything` —— 2/5 个有
- `GetNode` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 5 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | sa_solver | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
