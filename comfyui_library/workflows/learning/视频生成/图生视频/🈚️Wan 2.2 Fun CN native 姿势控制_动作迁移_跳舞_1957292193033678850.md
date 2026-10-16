---
key: 视频生成/图生视频/🈚️Wan 2.2 Fun CN native 姿势控制_动作迁移_跳舞_1957292193033678850.json
name: 🈚️Wan 2.2 Fun CN native 姿势控制_动作迁移_跳舞_1957292193033678850.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1957292193033678850.json
hash: 414620aee2bd3821
coverage: 0.45614
learned_at: 2026-10-15 22:31:16
nodes: [UNETLoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Prompt Text, WanMoeKSampler, ApplySageAttention, VAELoader, SetNode, CLIPTextEncode, SetNode, CLIPTextEncode, SetNode, SetNode, SetNode, Int, Int, Wan22FunControlToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, SetNode, SetNode, ImageScale, GetNode, GetNode, GetImageSize, GetNode, ImageScale, SetNode, LoadImage, VHS_LoadVideo, SetNode, GetNode, AIO_Preprocessor, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, VHS_VideoCombine, Int, SetNode, Int, VHS_VideoCombine, GetNode, ApplySageAttention, GetNode, GetNode, SetNode, SetNode, SetNode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/🈚️Wan 2.2 Fun CN native 姿势控制_动作迁移_跳舞_1957292193033678850.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957292193033678850.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（57 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `WanMoeKSampler` ★核心
- `ApplySageAttention`
- `VAELoader`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `Int`
- `Wan22FunControlToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `ImageScale`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `ImageScale`
- `SetNode`
- `LoadImage`
- `VHS_LoadVideo`
- `SetNode`
- `GetNode`
- `AIO_Preprocessor`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Int`
- `SetNode`
- `Int`
- `VHS_VideoCombine`
- `GetNode`
- `ApplySageAttention`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **46%**（26/57）

**有卡**：`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`CR Prompt Text`、`WanMoeKSampler`、`ApplySageAttention`、`VAELoader`、`CLIPTextEncode`、`Int`、`Wan22FunControlToVideo`、`VAEDecode`、`ImageScale`、`GetImageSize`、`LoadImage`、`VHS_LoadVideo`、`AIO_Preprocessor`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
