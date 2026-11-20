---
name: image_to_image_lora_sampler_unet_83
type: Image To Image
frequency: 9
level: strong
coverage: 0.840222
common_nodes: [CLIPLoader, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/🥯Qwen-next scene人物一致自动分镜控制🥯_1983051929599246337.json, 图片生成/文生图/qwen2509文生图短剧分镜图片_2010143977151930370.json, 图片生成/文生图/【微电影】镜头风格一致性电影3分镜 Qwen+Next+Scene+影视剧情分镜制作_1990302085990240258.json, 图片生成/文生图/【微电影】镜头风格一致性电影3分镜影视剧情分镜制作-邻家AI大女孩_2042485741443358721.json, 图片生成/文生图/【电影效果】人物一致性12分镜 影视剧情分镜制作_2106364207892615170.json, 图片生成/文生图/一键分镜，快速出图_1981898675020546049.json, 图片生成/文生图/一键分镜，快速出图_2028298848090722306.json, 图片生成/文生图/一键生成影视剧情分镜制作_2003128546249908226.json, 图片生成/文生图/全能版-根据主题自动分镜剧本图_1986359513102118913.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_83

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/🥯Qwen-next scene人物一致自动分镜控制🥯_1983051929599246337.json、图片生成/文生图/qwen2509文生图短剧分镜图片_2010143977151930370.json、图片生成/文生图/【微电影】镜头风格一致性电影3分镜 Qwen+Next+Scene+影视剧情分镜制作_1990302085990240258.json、图片生成/文生图/【微电影】镜头风格一致性电影3分镜影视剧情分镜制作-邻家AI大女孩_2042485741443358721.json、图片生成/文生图/【电影效果】人物一致性12分镜 影视剧情分镜制作_2106364207892615170.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
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
- `ProcessString` —— 8/9 个有
- `RH_LLMAPI_NODE` —— 8/9 个有
- `Anything Everywhere3` —— 7/9 个有
- `JjkText` —— 6/9 个有
- `ShellAgentPluginOutputText` —— 6/9 个有
- `PreviewImage` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `ImpactInt` —— 2/9 个有
- `JoinStringMulti` —— 2/9 个有
- `easy convertAnything` —— 2/9 个有
- `GetNode` —— 1/9 个有
- `Note Plus (mtb)` —— 1/9 个有
- `SetNode` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 9 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | sa_solver | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
