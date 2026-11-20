---
name: text_to_image_sampler_clip_unet_27
type: Text To Image
frequency: 16
level: moderate
coverage: 0.899
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/anima基础工作流_2050251032118210561.json, 图片生成/文生图/boogu base文生图_2067452727042592770.json, 图片生成/文生图/boogu image turbo 文生图_2069087085788749825.json, 图片生成/文生图/boogu turbo反推文生图_2070395337566679041.json, 图片生成/文生图/boogu turbo反推文生图_2070430959291428865.json, 图片生成/文生图/boogu turbo反推文生图无需提示词_2070351358628294658.json, 图片生成/文生图/boogu turbo反推文生图无需提示词_2070418685847760898.json, 图片生成/文生图/boogu turbo文生图_2069610874171641858.json, 图片生成/文生图/boogu turbo文生图_2069633350947663873.json, 图片生成/文生图/boogu turbo文生图_2069634712343244801.json, 图片生成/文生图/boogu turbo文生图急速生图_2069629401351933954.json, 图片生成/文生图/krea turbo反推文生图_2070393483688505346.json, 图片生成/文生图/krea2 文生图 工作流+全节点注释_2077385249922834434.json, 图片生成/文生图/厚涂cg风格-文生图-krea2_2077167625519583233.json, 图片生成/文生图/国漫cg风格-文生图-krea2_2077165275518160898.json, 图片生成/文生图/鬼刀画风-文生图-krea2_2076834870831181825.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_27

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/anima基础工作流_2050251032118210561.json、图片生成/文生图/boogu base文生图_2067452727042592770.json、图片生成/文生图/boogu image turbo 文生图_2069087085788749825.json、图片生成/文生图/boogu turbo反推文生图_2070395337566679041.json、图片生成/文生图/boogu turbo反推文生图_2070430959291428865.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 15/16 个有
- `CR Text` —— 9/16 个有
- `LoadImage` —— 6/16 个有
- `AILab_QwenVL` —— 5/16 个有
- `JjkText` —— 4/16 个有
- `LatentUpscaleBy` —— 4/16 个有
- `LoraLoader` —— 4/16 个有
- `PreviewAny` —— 4/16 个有
- `MultiTextConcatenate` —— 3/16 个有
- `OneButtonPrompt` —— 3/16 个有
- `FluxResolutionNode` —— 1/16 个有
- `LoaderGGUF` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1664 | 16 | 77% |
| 高度 | 1536 | 928 - 1536 | 16 | 82% |
| 采样步数 | 8 | 4 - 50 | 16 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 16 | 28% |
| 采样算法 | euler | - | 16 | 81% |
| 调度器 | simple | - | 16 | 88% |
| 重绘幅度 | 1 | 0.6 - 1 | 16 | 81% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1664，16 个样本
- 高度 中位数 1536，观测区间 928 - 1536，16 个样本，取值集中（一致性 82%）
- 采样步数 中位数 8，观测区间 4 - 50，16 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，16 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 euler，16 个样本，一致性 81%
- 调度器 最常用 simple，16 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，16 个样本，取值集中（一致性 81%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（18/16 个样本）：Steps较低可能导致细节不足
