---
name: unknown_workflow_video_lora_sampler_264
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.708
common_nodes: [CLIPLoader, CLIPTextEncode, DiffusionModelLoaderKJ, DiffusionModelSelector, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, TrimVideoLatent, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 VACE-comfyui官方版_1946855361778184193.json, 视频生成/图生视频/wan2.2首尾帧Fun VACE视频工作流效果嘎嘎棒_1967883312465326081.json, 视频生成/图生视频/wan2_2_fun_vace_controlvideo_1967231938215940098.json, 视频生成/图生视频/wan2_2_fun_vace_flfv_1967234477657350146.json, 视频生成/图生视频/wan2_2_fun_vace_refimg_1967218674518122497.json, 视频生成/图生视频/wan2_2_fun_vace_动作控制视频-自动提示词_1967612484775546881.json, 视频生成/图生视频/wan2_2_fun_vace_动作迁移+高清放大_1969262637538308098.json, 视频生成/图生视频/wan2_2_fun_vace_图片参考视频-自动提示词_1967609614747525122.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_264

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 VACE-comfyui官方版_1946855361778184193.json、视频生成/图生视频/wan2.2首尾帧Fun VACE视频工作流效果嘎嘎棒_1967883312465326081.json、视频生成/图生视频/wan2_2_fun_vace_controlvideo_1967231938215940098.json、视频生成/图生视频/wan2_2_fun_vace_flfv_1967234477657350146.json、视频生成/图生视频/wan2_2_fun_vace_refimg_1967218674518122497.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `DiffusionModelSelector`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 7/8 个有
- `ImageResizeKJv2` —— 7/8 个有
- `GetNode` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `RMBG` —— 5/8 个有
- `SetNode` —— 5/8 个有
- `Int` —— 4/8 个有
- `AIO_Preprocessor` —— 3/8 个有
- `Label (rgthree)` —— 3/8 个有
- `SimpleMath+` —— 3/8 个有
- `VHS_LoadVideo` —— 3/8 个有
- `WanVideoVACEStartToEndFrame` —— 3/8 个有
- `CR Text Replace` —— 2/8 个有
- `PrimitiveBoolean` —— 2/8 个有
- `TextBox` —— 2/8 个有
- `easy ifElse` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `AILab_MiniCPM_4_V_Advanced` —— 1/8 个有
- `CR Image Input Switch` —— 1/8 个有
- `CR Text Concatenate` —— 1/8 个有
- `ImageResizeKJ` —— 1/8 个有
- `ImpactSwitch` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `RH_Captioner` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 16 | 8 | 71% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | lcm | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 16，8 个样本
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 16，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
