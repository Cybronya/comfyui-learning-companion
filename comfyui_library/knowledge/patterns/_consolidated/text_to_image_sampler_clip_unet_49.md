---
name: text_to_image_sampler_clip_unet_49
type: Text To Image
frequency: 13
level: moderate
coverage: 0.954769
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image文生图art_2017930293285490690.json, 图片生成/文生图/Z-image文生图：超细腻写实质感+精准文字渲染_1994608742673096706.json, 图片生成/文生图/Z-image新王登基君临天下(文生图)_1993946984736292866.json, 图片生成/文生图/Z-image，文生图_1995081308172955649.json, 图片生成/文生图/Zimage_Turbo尺寸控制器版_2073283589403402242.json, 图片生成/文生图/Zimage_Turbo经典版_2047589392318992385.json, 图片生成/文生图/krea2_turbo_基础文生图工作流_2078078374207115266.json, 图片生成/文生图/krea2基础文生图_2071164326781734914.json, 图片生成/文生图/krea2基础文生图文生图工作流_2089571734700773377.json, 图片生成/文生图/krea2基础文生图高清出图工作流_2089673479443533826.json, 图片生成/文生图/krea2文生图_2087794601284431873.json, 图片生成/文生图/文生图 Qwen Image 2512_2031964505944625153.json, 平台全量/字韵交织 · 形意共生的标志构成法则_2081912021586636802.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_49

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Z-image文生图art_2017930293285490690.json、图片生成/文生图/Z-image文生图：超细腻写实质感+精准文字渲染_1994608742673096706.json、图片生成/文生图/Z-image新王登基君临天下(文生图)_1993946984736292866.json、图片生成/文生图/Z-image，文生图_1995081308172955649.json、图片生成/文生图/Zimage_Turbo尺寸控制器版_2073283589403402242.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 12/13 个有
- `LoraLoaderModelOnly` —— 9/13 个有
- `Int` —— 6/13 个有
- `Text Multiline` —— 3/13 个有
- `ImpactSwitch` —— 2/13 个有
- `easy promptLine` —— 2/13 个有
- `GetNode` —— 1/13 个有
- `INTConstant` —— 1/13 个有
- `LatentFrequencyEnhancer_lrzjason` —— 1/13 个有
- `QwenImageLatentAspectRatio` —— 1/13 个有
- `RH_LLMAPI_NODE` —— 1/13 个有
- `SetNode` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 10 | 13 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 38% |
| 调度器 | simple | - | 13 | 77% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 1080 | 512 - 1920 | 13 | 67% |
| 高度 | 1536 | 512 - 2368 | 13 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 10，13 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 38%
- 调度器 最常用 simple，13 个样本，一致性 77%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 512 - 1920，13 个样本
- 高度 中位数 1536，观测区间 512 - 2368，13 个样本
- 高发问题（7/13 个样本）：Steps较低可能导致细节不足
