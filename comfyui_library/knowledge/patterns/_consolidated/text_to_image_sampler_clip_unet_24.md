---
name: text_to_image_sampler_clip_unet_24
type: Text To Image
frequency: 16
level: moderate
coverage: 0.723437
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, PreviewAny, PrimitiveStringMultiline, SaveImage, StringConcatenate, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 Instagram 摄影风格文生图_2087916354635649025.json, 图片生成/文生图/Krea2 Raw文生图V1_2069649846545506305.json, 图片生成/文生图/Krea2 Raw文生图V1_2069955897165697025.json, 图片生成/文生图/Krea2 Raw版-文生图-v1.0_2070040927531528193.json, 图片生成/文生图/Krea2 Turbo Realism Engineer V2文生图_2072187241404911618.json, 图片生成/文生图/Krea2 Turbo Realism Engineer V2文生图_2072504382511476738.json, 图片生成/文生图/Krea2 Turbo Realism Engineer文生图_2072366906035761153.json, 图片生成/文生图/Krea2 Turbo 单色水墨风格文生图_2078458901254725633.json, 图片生成/文生图/Krea2 Turbo 文生图 极速写实摄影工作流_2072318540417425410.json, 图片生成/文生图/Krea2 Turbo 柔和极简素描风格文生图_2078480779449032705.json, 图片生成/文生图/Krea2 Turbo 真实感写实风格文生图_2078379281394257921.json, 图片生成/文生图/Krea2 Turbo 空灵闪耀光风格文生图_2078478130687336450.json, 图片生成/文生图/Krea2 Turbo 青绿色水彩插画风格文生图_2078398716591042562.json, 图片生成/文生图/Krea2 Turbo文生图(wlop）lora_2070665195122413570.json, 图片生成/文生图/Krea2 Turbo文生图+全节点注释_2072663092810575873.json, 图片生成/文生图/极速美学版-Krea2 Turbo-文生图-美学不错_2070037389308944386.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_24

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/Krea2 Instagram 摄影风格文生图_2087916354635649025.json、图片生成/文生图/Krea2 Raw文生图V1_2069649846545506305.json、图片生成/文生图/Krea2 Raw文生图V1_2069955897165697025.json、图片生成/文生图/Krea2 Raw版-文生图-v1.0_2070040927531528193.json、图片生成/文生图/Krea2 Turbo Realism Engineer V2文生图_2072187241404911618.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `SaveImage`
- `StringConcatenate`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 12/16 个有
- `LoraLoaderModelOnly` —— 12/16 个有
- `ResolutionSelector` —— 10/16 个有
- `JWInteger` —— 6/16 个有
- `ImageConcanate` —— 3/16 个有
- `LoadImage` —— 3/16 个有
- `CR Prompt Text` —— 1/16 个有
- `CR Text` —— 1/16 个有
- `TextConcat` —— 1/16 个有
- `easy promptLine` —— 1/16 个有
- `easy showAnything` —— 1/16 个有
- `孤海注释` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 16 | 100% |
| 高度 | 1024 | 1024 - 1024 | 16 | 100% |
| 采样步数 | 8 | 8 - 28 | 16 | 35% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 16 | 34% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，16 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 28，16 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，16 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（15/16 个样本）：Steps较低可能导致细节不足
