---
key: 视频生成/图生视频/ComfyUI_InteractAvatar 基础工作流_2021465868349218818.json
name: ComfyUI_InteractAvatar 基础工作流_2021465868349218818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/ComfyUI_InteractAvatar 基础工作流_2021465868349218818.json
hash: 151954b898aebf3d
coverage: 0.886364
learned_at: 2026-10-15 22:35:08
nodes: [VAEDecode, VAEDecode, CLIPLoader, InteractAvatar_SM_Sampler, CreateVideo, CLIPLoader, InteractAvatar_SM_Sampler, CreateVideo, InteractAvatar_SM_Model, SaveVideo, VAEDecode, CLIPLoader, InteractAvatar_SM_Sampler, CreateVideo, InteractAvatar_SM_Model, SaveVideo, SaveImage, GetVideoComponents, Note, Note, Note, Note, SaveVideo, Note, InteractAvatar_SM_Model, VAELoader, LoadImage, LoadImage, LoadAudio, InteractAvatar_SM_Predata, LoadImage, LoadImage, LoadAudio, VAELoader, LoadImage, InvertMask, InteractAvatar_SM_Predata, VAELoader, LoadAudio, InvertMask, LoadImage, InteractAvatar_SM_Predata, LoadVideo, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/ComfyUI_InteractAvatar 基础工作流_2021465868349218818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2021465868349218818.json`

## 结构

**生成流程**：Model → Sampling → Decode → Output → Other

**节点**（44 个）：
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `InteractAvatar_SM_Sampler` ★核心
- `CreateVideo`
- `CLIPLoader`
- `InteractAvatar_SM_Sampler` ★核心
- `CreateVideo`
- `InteractAvatar_SM_Model`
- `SaveVideo`
- `VAEDecode` ★核心
- `CLIPLoader`
- `InteractAvatar_SM_Sampler` ★核心
- `CreateVideo`
- `InteractAvatar_SM_Model`
- `SaveVideo`
- `SaveImage`
- `GetVideoComponents`
- `Note`
- `Note`
- `Note`
- `Note`
- `SaveVideo`
- `Note`
- `InteractAvatar_SM_Model`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `InteractAvatar_SM_Predata`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `VAELoader`
- `LoadImage`
- `InvertMask`
- `InteractAvatar_SM_Predata`
- `VAELoader`
- `LoadAudio`
- `InvertMask`
- `LoadImage`
- `InteractAvatar_SM_Predata`
- `LoadVideo`
- `VHS_LoadVideo`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`VAEDecode`、`CLIPLoader`、`InteractAvatar_SM_Sampler`、`CreateVideo`、`InteractAvatar_SM_Model`、`SaveVideo`、`SaveImage`、`GetVideoComponents`、`VAELoader`、`LoadImage`、`LoadAudio`、`InteractAvatar_SM_Predata`、`InvertMask`、`LoadVideo`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、LoadImage、InteractAvatar_SM_Sampler、SaveImage、SaveVideo、CreateVideo
