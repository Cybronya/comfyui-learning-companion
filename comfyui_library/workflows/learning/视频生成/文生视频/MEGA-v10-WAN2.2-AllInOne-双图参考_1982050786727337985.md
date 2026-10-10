---
key: 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-双图参考_1982050786727337985.json
name: MEGA-v10-WAN2.2-AllInOne-双图参考_1982050786727337985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-双图参考_1982050786727337985.json
hash: f42eb0cdf82b4a7d
coverage: 0.904762
learned_at: 2026-10-11 02:45:00
nodes: [TrimVideoLatent, VAEDecode, ModelSamplingSD3, VHS_VideoCombine, CLIPTextEncode, INTConstant, WanVaceToVideo, CLIPTextEncode, ImageConcanate, INTConstant, INTConstant, Image Rembg (Remove Background), Image Rembg (Remove Background), TTP_Expand_And_Mask, TTP_Expand_And_Mask, LoadImage, KSampler, CLIPLoader, AV_VAELoader, UNETLoader, LoadImage]
patterns: []
missing: [Image Rembg (Remove Background), Image Rembg (Remove Background)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 192054346835137, "steps": 4}
discoveries: [次要节点 `Image Rembg (Remove Background)` 知识库中没有该节点类型的任何知识, 次要节点 `Image Rembg (Remove Background)` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-双图参考_1982050786727337985.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-双图参考_1982050786727337985.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（21 个）：
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `ImageConcanate`
- `INTConstant`
- `INTConstant`
- `Image Rembg (Remove Background)`
- `Image Rembg (Remove Background)`
- `TTP_Expand_And_Mask`
- `TTP_Expand_And_Mask`
- `LoadImage`
- `KSampler` ★核心
- `CLIPLoader`
- `AV_VAELoader`
- `UNETLoader` ★核心
- `LoadImage`

## 关键参数

- `seed` = `192054346835137`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`TrimVideoLatent`、`VAEDecode`、`ModelSamplingSD3`、`VHS_VideoCombine`、`CLIPTextEncode`、`INTConstant`、`WanVaceToVideo`、`ImageConcanate`、`TTP_Expand_And_Mask`、`LoadImage`、`KSampler`、`CLIPLoader`、`AV_VAELoader`、`UNETLoader`

**缺卡**（2）：`Image Rembg (Remove Background)`、`Image Rembg (Remove Background)`

**用到的条目**：KSampler、VAEDecode、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、TrimVideoLatent、AV_VAELoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Image Rembg (Remove Background)` 知识库中没有该节点类型的任何知识
- 次要节点 `Image Rembg (Remove Background)` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
