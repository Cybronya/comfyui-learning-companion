---
name: image_to_image_lora_sampler_unet_60
type: Image To Image
frequency: 10
level: strong
coverage: 0.8591
common_nodes: [CLIPLoader, CR Prompt List, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ProcessString, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2509场景多角度分镜制作镜头风格一致性分镜加速版_2054480221952331778.json, 图片生成/图生图/Qwen2509巅峰赋能：多场景分镜输出，风格一致性绝对制霸_1987162767272644610.json, 图片生成/图生图/Qwen专用场景多角度镜头_2014687187824025602.json, 图片生成/图生图/Qwen多角度一致性_2003674616868577281.json, 图片生成/图生图/【CQ808】场景多角度镜头风格_2010666611983781889.json, 图片生成/图生图/【CQ808】巨日禄专用场景多角度镜头V.10_2011797751985610754.json, 图片生成/图生图/史上最最最强一键生成多角度、多镜头控制工作流_1986826718788972546.json, 图片生成/图生图/场景多角度_1990615866486263810.json, 图片生成/图生图/场景多角度分镜2.0制作镜头qwen2511风格一致性分镜加速版(3)_2003652314483335170.json, 图片生成/文生图/千问Qwen2509超强自定义短剧分镜一致性_1988465961592340482.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_60

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen2509场景多角度分镜制作镜头风格一致性分镜加速版_2054480221952331778.json、图片生成/图生图/Qwen2509巅峰赋能：多场景分镜输出，风格一致性绝对制霸_1987162767272644610.json、图片生成/图生图/Qwen专用场景多角度镜头_2014687187824025602.json、图片生成/图生图/Qwen多角度一致性_2003674616868577281.json、图片生成/图生图/【CQ808】场景多角度镜头风格_2010666611983781889.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt List`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ProcessString`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 9/10 个有
- `Text Multiline` —— 8/10 个有
- `CR Text` —— 3/10 个有
- `Float` —— 2/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `GetNode` —— 1/10 个有
- `SetNode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | sa_solver | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
