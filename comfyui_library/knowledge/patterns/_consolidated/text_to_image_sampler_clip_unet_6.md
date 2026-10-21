---
name: text_to_image_sampler_clip_unet_6
type: Text To Image
frequency: 22
level: moderate
coverage: 0.938045
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/千问qwen-2512文生图（自定义尺寸）_2083196882171547649.json, 图片生成/文生图/千问文生图4步加速工作流_2011421425135001601.json, 图片生成/文生图/千问文生图工作流_1992469322945851393.json, 图片生成/文生图/千问文生图工作流_2003750459162673154.json, 图片生成/文生图/厚涂cg插画风格zimage_2005084819052785665.json, "图片生成/文生图/图图的 8D 极光黑丝 Z-Image 工作流_Tutu's Aurora 8D HiSilk Z-Image workflow_2070753635646136322.json", "图片生成/文生图/图图的 PVC 护士服 Z-Image 工作流_Tutu's PVC Nurse Outfit Z-Image workflow_2070438619709526017.json", "图片生成/文生图/图图的大网渔网袜 Z-Image 工作流_Tutu's HiSilk Fishnet Z-Image workflow_2070751109303586818.json", "图片生成/文生图/图图的洛丽塔黑江雫服装工作流_Tutu's Lolita Shizuku Kuroe Outfit workflow_2070374570158284801.json", 图片生成/文生图/图图的炫彩 Anima 工作流_Tutu Colorburst Anima workflow_2070527633288421378.json, 图片生成/文生图/图图的炫彩 Anima 工作流_Tutu Colorburst Anima workflow_2070744860063256578.json, "图片生成/文生图/图图的碧蓝幻想风格 Anima 工作流_Tutu's Blue Fantasy Style Anima workflow_2070439368904503298.json", "图片生成/文生图/图图的维琳娜·艾嘉德ANIMA专属工作流_Tutu's Velina Airgid Anima_2068357227324469249.json", "图片生成/文生图/图图的艾尔妲·挽昼专属工作流_Tutu's Eldreda Sunbringer workflow_2070126352094810114.json", "图片生成/文生图/图图的蕾米埃尔·丹工作流_Tutu's Remielle Dan workflow_2069063026359234561.json", "图片生成/文生图/图图的长款旗袍风蕾丝连衣裙工作流_Tutu's Long Qipao Lace Dress workflow_2070419601577570306.json", "图片生成/文生图/图图的黑色配饰连体服 Z-Image 工作流_Tutu's HiSilk Black Accessories Z-Image workflow_2070527635050033153.json", "图片生成/文生图/图图的黑色配饰连体服 Z-Image 工作流_Tutu's HiSilk Black Accessories Z-Image workflow_2070749678974627841.json", 图片生成/文生图/文生图-krea2_2069932258559086593.json, 图片生成/文生图/文生图-rh-Z-image-超清_2013965047239806978.json, 图片生成/文生图/文生图ZIT_2025848646826205185.json, 图片生成/文生图/电商文生图 krea2_2079494663781834754.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_6

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/文生图/千问qwen-2512文生图（自定义尺寸）_2083196882171547649.json、图片生成/文生图/千问文生图4步加速工作流_2011421425135001601.json、图片生成/文生图/千问文生图工作流_1992469322945851393.json、图片生成/文生图/千问文生图工作流_2003750459162673154.json、图片生成/文生图/厚涂cg插画风格zimage_2005084819052785665.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 17/22 个有
- `ConditioningZeroOut` —— 10/22 个有
- `CLIPSetLastLayer` —— 1/22 个有
- `FlashVSRNode` —— 1/22 个有
- `JjkText` —— 1/22 个有
- `RH_Translator` —— 1/22 个有
- `TextEncodeQwenImageEditPlus` —— 1/22 个有
- `ZImageLoraModelOnly` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | 832 - 1920 | 22 | 82% |
| 高度 | 1520 | 720 - 1920 | 22 | 76% |
| 采样步数 | 10 | 2 - 45 | 22 | 25% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 22 | 37% |
| 采样算法 | euler | - | 22 | 32% |
| 调度器 | simple | - | 22 | 59% |
| 重绘幅度 | 1 | 0.2 - 1 | 22 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1052，观测区间 832 - 1920，22 个样本，取值集中（一致性 82%）
- 高度 中位数 1520，观测区间 720 - 1920，22 个样本
- 采样步数 中位数 10，观测区间 2 - 45，22 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，22 个样本，取值分散，一致性仅 37%
- 采样算法 最常用 euler，22 个样本，一致性 32%
- 调度器 最常用 simple，22 个样本，一致性 59%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，22 个样本，取值集中（一致性 83%）
