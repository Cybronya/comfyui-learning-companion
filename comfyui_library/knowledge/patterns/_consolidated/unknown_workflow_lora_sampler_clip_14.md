---
name: unknown_workflow_lora_sampler_clip_14
type: Unknown Workflow
frequency: 27
level: strong
coverage: 0.846667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Lora+提示词=风格化图片_1952911676233478146.json, 图片生成/文生图/像素风格插画_1912796321265217537.json, 图片生成/文生图/泡泡液态金属字体_2047922074966036481.json, 图片生成/文生图/游戏道具工具箱工作流_1992976015037235201.json, 图片生成/文生图/美食类游戏蛋糕_1866768530052988929.json, 图片生成/文生图/黏土风icon_1955200823770976258.json, 平台全量/3D ICON图标_1866778066549964801.json, 平台全量/3D动漫玩偶三视图_1866368829117853697.json, 平台全量/FLUX.吴冠中水乡风CNGHWCS_1937072905937391617.json, 平台全量/IP形象丨透明机械质感_1962753919430574082.json, 平台全量/【基础流】Flux国风-水墨速写_1867416325277843458.json, 平台全量/【基础流】马克笔风格插画_1867037067954864130.json, 平台全量/万花筒玻璃折射_1937804949558312961.json, 平台全量/云端上的毛绒绒_1938525269692973057.json, 平台全量/动物足球联赛_1937802846949523458.json, 平台全量/国潮风格插画_1866429660882956289.json, 平台全量/扁平风格插画_1866356518546526210.json, 平台全量/手绘简笔画风格插画_1866429237275029506.json, 平台全量/毛绒风格插画_1866678880974360577.json, 平台全量/浮世绘风格插画_1866687278356844546.json, 平台全量/游戏道具工具箱_1866767961137840129.json, 平台全量/游戏道具武器箱_1866721856425193473.json, 平台全量/游戏道具注射器_1866767459792351233.json, 平台全量/矢量风格插画_1866755729364570113.json, 平台全量/肌理感插画_1866402697791623170.json, 平台全量/胶片摄影 F.1_ 电影镜头_1937063778401832962.json, 平台全量/超现实风格插画_1866403043532296194.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（图片生成/文生图/Lora+提示词=风格化图片_1952911676233478146.json、图片生成/文生图/像素风格插画_1912796321265217537.json、图片生成/文生图/泡泡液态金属字体_2047922074966036481.json、图片生成/文生图/游戏道具工具箱工作流_1992976015037235201.json、图片生成/文生图/美食类游戏蛋糕_1866768530052988929.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 27 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 26/27 个有
- `JjkText` —— 26/27 个有
- `PreviewImage` —— 26/27 个有
- `TextCombinerTwo` —— 26/27 个有
- `CheckpointLoaderSimple` —— 23/27 个有
- `Label (rgthree)` —— 17/27 个有
- `ImageUpscaleWithModel` —— 5/27 个有
- `RH_Translator` —— 5/27 个有
- `ShowText|pysssss` —— 5/27 个有
- `UpscaleModelLoader` —— 5/27 个有
- `LayerColor: Brightness & Contrast` —— 4/27 个有
- `RH_Prompter` —— 4/27 个有
- `UNETLoader` —— 4/27 个有
- `VAEEncode` —— 4/27 个有
- `DeepTranslatorTextNode` —— 3/27 个有
- `CR String To Combo` —— 1/27 个有
- `Primitive string [Crystools]` —— 1/27 个有
- `Text Multiline` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1024 | 27 | 93% |
| 高度 | 1280 | 1024 - 1536 | 27 | 93% |
| LoRA 模型强度 | 1 | 0.45 - 1.2 | 27 | 83% |
| LoRA 文本强度 | 1 | 0.75 - 1 | 27 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1024，27 个样本，取值集中（一致性 93%）
- 高度 中位数 1280，观测区间 1024 - 1536，27 个样本，取值集中（一致性 93%）
- LoRA 模型强度 中位数 1，观测区间 0.45 - 1.2，27 个样本，取值集中（一致性 83%）
- LoRA 文本强度 中位数 1，观测区间 0.75 - 1，27 个样本，取值集中（一致性 92%）
