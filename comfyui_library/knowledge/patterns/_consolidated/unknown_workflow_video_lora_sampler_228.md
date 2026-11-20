---
name: unknown_workflow_video_lora_sampler_228
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.578091
common_nodes: [BerniniConditioning, CLIPLoader, CLIPTextEncode, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, WanVideoNAG]
problems: []
missing: []
members: [平台全量/Berinini_人物替换_动作迁移_2075390746320007169.json, 平台全量/电商视频换服装 wan2.2 bernini_2061072367056670722.json, 平台全量/电商视频换服装 wan2.2 bernini_2067092091255222273.json, 数字人/数字人/Berinini版-无限时长-带货数字人替换_2074707187401838593.json, 视频生成/图生视频/video_wan2_2_bernini_rv2v_add_2064247414655115266.json, 视频生成/图生视频/video_wan2_2_bernini_rv2v_replace_2064232122084319234.json, 视频生成/文生视频/video_wan2_2_bernini_i2i_2064270918700060673.json, 视频生成/文生视频/video_wan2_2_bernini_multi_r2v_2064268091416207362.json, 视频生成/文生视频/video_wan2_2_bernini_r2v_2064265816681570306.json, 视频生成/文生视频/video_wan2_2_bernini_rv2v_change_style_2064258770699636737.json, 视频生成/文生视频/video_wan2_2_bernini_rv2v_changebg_2064251615900688385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_228

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/Berinini_人物替换_动作迁移_2075390746320007169.json、平台全量/电商视频换服装 wan2.2 bernini_2061072367056670722.json、平台全量/电商视频换服装 wan2.2 bernini_2067092091255222273.json、数字人/数字人/Berinini版-无限时长-带货数字人替换_2074707187401838593.json、视频生成/图生视频/video_wan2_2_bernini_rv2v_add_2064247414655115266.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 11 个 workflow 都包含：
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 10/11 个有
- `CFGZeroStar` —— 9/11 个有
- `INTConstant` —— 8/11 个有
- `BatchImagesNode` —— 7/11 个有
- `CLIPVisionLoader` —— 7/11 个有
- `GetNode` —— 7/11 个有
- `SetNode` —— 7/11 个有
- `JjkText` —— 2/11 个有
- `WanContextWindowsManual` —— 2/11 个有
- `easy imageRemBg` —— 2/11 个有
- `Float` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `PrimitiveInt` —— 1/11 个有
- `PrimitiveStringMultiline` —— 1/11 个有
- `SaveImage` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 82% |
| Prompt 约束强度(CFG) | 6 | 4 - 10 | 11 | 78% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | lcm | - | 11 | 82% |
| 重绘幅度 | simple | - | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 82%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 10，11 个样本
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，11 个样本，一致性 82%
- 重绘幅度 最常用 simple，11 个样本，一致性 100%
